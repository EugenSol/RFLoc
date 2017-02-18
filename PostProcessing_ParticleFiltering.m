%% Compute receiver position from signal strength measurements
%% Input: Text file with signal strengths

clear all
Imported = importdata('rectangle_2017_02_17_inner_sample256_3_.txt',',');

time = Imported.data(:,2);
x_true = Imported.data(:,3);
y_true = Imported.data(:,4);

RSS_1 = Imported.data(:,5);
RSS_2 = Imported.data(:,6);
RSS_3 = Imported.data(:,7);
RSS_4 = Imported.data(:,8);

tx_pos = [1060, 475; 1060, 1270; 2340, 475; 2340, 1270]; %manually set

%range sensor model parameters, obtained from calibration
alpha = [0.014709602541178866, 0.0077900690750465108, 0.021332643097358831, 0.01927141735523798]; 
gamma = [-4.1078304251509863, -1.0803810035095545, -8.8011430617526756, -7.5502754274383337];

%number of particles
numP = 1000;

%measurement std
meas_std = 1;    %in dBm
proc_std_x = 20;   %in mm
proc_std_y = 20;   %in mm

%time horizon
T = size(RSS_1,1);

%particle weights ini
w_unnormalized = zeros(numP,1);   %unnormalized
w = zeros(numP,1);		  %normalized

r_x = 1300 + (2400-(1300)).*rand(numP*100,1);           %initial distribution for x
r_y = 500 + (1100-(500)).*rand(numP*100,1);           %initial distribution for y

thetaf = zeros(numP,T,2);                     %(numP, t, [x y])
thetap = zeros(numP,T,2);

%Step 1: Sample from initial distribution
thetaf(:,1,1) = randsample(r_x,numP);      %x    
thetaf(:,1,2) = randsample(r_y,numP);      %y

clear r_x r_y

for t = 2:T   %loop through data set
    
    	% Particle Proposal via random walk
        thetap(:,t,1) = thetaf(:,t-1,1)+ random('normal', 0, proc_std_x, numP, 1);    %x
        thetap(:,t,2) = thetaf(:,t-1,2)+ random('normal‘, 0, proc_std_y, numP, 1);    %y
        
	% propagate particle through measurement equation to obtain predicted RSS for each particle
        RSS_pred = zeros(numP, 4);
        for i = 1:4
            for p = 1 : numP
                R_i = norm(squeeze(thetap(p,t,:)) - tx_pos(i,:)');
                RSS_pred(p, i) = -20*log10(R_i) - alpha(i) * R_i - gamma(i) ;
            end
        end
        
	%Compute unnormalized weights
        w_unnormalized(:,1) = normpdf( RSS_1(t), RSS_pred(:,1), meas_std^2 ).*normpdf( RSS_2(t), RSS_pred(:,2), meas_std^2 ).*normpdf( RSS_3(t), RSS_pred(:,3), meas_std^2 ).*normpdf( RSS_4(t), RSS_pred(:,4), meas_std^2 );

	%Normalize weights
        w(:,1) = w_unnormalized(:,1).*1/sum(w_unnormalized(:,1));                             

	% Resample particles according to weights
        idx(:,1) = randsample([1:numP],numP,true,w(:,1)');
        thetaf(:,t,:) = thetap(idx,t,:);
        
end


% Compute particle means
for l =1:T
    x(l) = sum(thetaf(:,l,1))/length(thetaf(:,l,1));
    y(l) = sum(thetaf(:,l,2))/length(thetaf(:,l,2));
end


% Plots
% plot ground truth
plot(x_true, y_true, 'r*');
hold on 

% plot particle means
plot(x, y, '*')

% plot beacon positions
hold on 
plot(tx_pos(:,1), tx_pos(:,2),'go')