from matplotlib.pyplot import figure, xlabel, ylabel

[x,y] = meshgrid(0:.05:3);

a1 = 1;
a2 = 1;
b1 = 5;
b2 = 1.5;
d  = .7;

#Fungsi Kepadatan Peluang Weibull Bivariat
pdfbiv = ((b1*b2)/(a1*a2))*((x/a1).^((b1/d)-1)).*((y/a2).^((b2/d)-1)).*(((x/a1).^(b1/d)+(y/a2).^(b2/d)).^(d-2)).*...
    ((((x/a1).^(b1/d)+(y/a2).^(b2/d)).^(d))+(1/d)-1).*exp(-(((((x)/a1).^(b1/d)+((y)/a2).^(b2/d)).^(d))));

figure(1)
surfc(pdfbiv);
title('Plot Fungsi Kepadatan Peluang Weibull Bivariat')
xlabel('x ; \alpha_x=1; \beta_x=5')
ylabel('y; \alpha_y=1; \beta_y=1,5')
zlabel('f(x,y); \delta=0.7')

#Fungsi Distribusi Kumulatif Weibull Bivariat
cdfbiv = 1-exp(-((x/a1).^(b1/d)+(y/a2).^(b2/d)).^d);

figure(2)
surfc(cdfbiv);
title('Plot Fungsi Distribusi Kumulatif Weibull Bivariat')
xlabel('x ; \alpha_x=1; \beta_x=5')
ylabel('y; \alpha_y=1; \beta_y=1,5')
zlabel('F(x,y); \delta=0.7')

#Fungsi Survival Weibull Bivariat
sdfbiv = exp(-((x/a1).^(b1/d)+(y/a2).^(b2/d)).^d);

figure(3)
surfc(sdfbiv);
title('Plot Fungsi Survival Weibull Bivariat')
xlabel('x ; \alpha_x=1; \beta_x=5')
ylabel('y; \alpha_y=1; \beta_y=1,5')
zlabel('S(x,y); \delta=0.7')

#Fungsi Hazard Weibull Bivariat
hzrdbiv = ((b1*b2)/(a1*a2))*((x/a1).^((b1/d)-1)).*((y/a2).^((b2/d)-1)).*(((x/a1).^(b1/d)+(y/a2).^(b2/d)).^(d-2)).*...
    ((((x/a1).^(b1/d)+(y/a2).^(b2/d)).^(d))+(1/d)-1);

figure(4)
surfc(hzrdbiv);
title('Plot Fungsi Hazard Weibull Bivariat')
xlabel('x ; \alpha_x=1; \beta_x=5')
ylabel('y; \alpha_y=1; \beta_y=1,5')
zlabel('h(x,y); \delta=0.7')

#Fungsi Hazard Kumulatif Weibull Bivariat
cfrbiv = ((x/a1).^(b1/d)+(y/a2).^(b2/d)).^d;

figure(5)
surfc(cfrbiv);
title('Plot Fungsi Hazard Kumulatif Weibull Bivariat')
xlabel('x ; \alpha_x=1; \beta_x=5')
ylabel('y; \alpha_y=1; \beta_y=1,5')
zlabel('H(x,y); \delta=0.7')