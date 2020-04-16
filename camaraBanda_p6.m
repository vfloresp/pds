load('filtro1.mat')
load('filtro2.mat')
load('filtro3.mat')
load('filtro4.mat')
load('filtro5.mat')
load('filtro6.mat')
load('filtro7.mat')
load('filtro8.mat')

Fs = 1000;                           
T = 1/Fs;                
L = 1500;             
t = (0:L-1)*T;        
S = 0.7*sin(2*pi*50*t) + sin(2*pi*120*t);
X = S + 2*randn(size(t));
plot(1000*t(1:50),X(1:50))

Y = fft(X);
f = Fs*(0:L-1)/L;

figure
Filtro1 = fft(Num);
resp1 =  conv(Y,Filtro1);
plot(abs(resp1)) 

figure
Filtro2 = fft(Num2);
resp2 =  conv(Y,Filtro2);
plot(abs(resp2))

figure
Filtro3 = fft(Num3);
resp3 =  conv(Y,Filtro3);
plot(abs(resp2)) 

figure
Filtro4 = fft(Num3);
resp4 =  conv(Y,Filtro4);
plot(abs(resp4)) 

figure
Filtro5 = fft(Num4);
resp5 =  conv(Y,Filtro5);
plot(abs(resp5)) 

figure
Filtro6 = fft(Num5);
resp6 =  conv (Y,Filtro6);
plot(abs(resp6)) 

figure
Filtro7 = fft(Num6);
resp7 =  conv (Y,Filtro7);
plot(abs(resp7)) 

figure
Filtro8 = fft(Num7);
resp8 =  conv (Y,Filtro8);
plot(abs(resp8)) 
