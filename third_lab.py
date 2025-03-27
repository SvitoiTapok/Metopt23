import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
def func(x):
    return np.log(1+x**2)-np.sin(x)

def quadrantic_approx(f, x1, delta_x, accuracy1, accuracy2):
    i = 0
    x2 = x1 + delta_x
    fx1 = f(x1)
    fx2 = f(x2)
    if fx1 > fx2:
        x3 = x1 + 2*delta_x
    else:
        x3 = x1 - delta_x
    while True:
        i += 1
        print("iter№", i)
        fx1 = f(x1)
        fx2 = f(x2)
        fx3 = f(x3)
        f_min = min(fx1, fx2, fx3)
        if f_min==fx1:
            x_min = x1
        if f_min==fx2:
            x_min = x2
        if f_min==fx3:
            x_min = x3

        znamen = (x2 - x3)*fx1 + (x3 - x1)*fx2 + (x1 - x2)*fx3
        print('x1:',x1,'x2:', x2,'x3:', x3,'fx1:', fx1,'fx2:', fx2,'fx3:', fx3,'x_min:', x_min,'f_min:', f_min,'znamenatel:', znamen)
        if znamen == 0:
            x1 = x_min
            x2 = x1 + delta_x
            fx1 = f(x1)
            fx2 = f(x2)
            if fx1 > fx2:
                x3 = x1 + 2*delta_x
            else:
                x3 = x1 - delta_x
            continue
        x_per = 1/2 * ((x2**2 - x3**2)*fx1 + (x3**2 - x1**2)*fx2 + (x1**2 - x2**2)*fx3) / znamen

        fxp = f(x_per)

        if fxp != 0:
            func_razn = abs((f_min - fxp) / fxp) < accuracy1
        else:
            func_razn = False
        if x_per != 0:
            arf_razn = abs((x_min - x_per) / x_per) < accuracy2
        else:
            arf_razn = False
        print('x_per:', x_per,'f(x_per):', fxp,'func_pogr:', abs((f_min - fxp) / fxp),'arg_pogr:', abs((x_min - x_per) / x_per))
        if func_razn and arf_razn:
            return [float(x_per), float(fxp), i]
        all_xs = [x1, x2, x3, x_per, x_min]
        left = min(x1, x3)
        right = max(x1, x3)
        if left <= x_per <= right:
            if(f_min<fxp):
                x2 = x_min
            else:
                x2 = x_per
            x1 = max(list(filter(lambda k: k < x2, all_xs)))
            x3 = min(list(filter(lambda k: k > x2, all_xs)))
            continue
        else:
            x1 = x_per
            x2 = x1 + delta_x
            fx1 = f(x1)
            fx2 = f(x2)
            if fx1 > fx2:
                x3 = x1 + 2*delta_x
            else:
                x3 = x1 - delta_x


print("Ответ:", quadrantic_approx(func, np.pi/8, 0.5, 0.03, 0.0003))