import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

def unipolar(inp):
    inp1 = list(inp)
    inp1.insert(0, '0')
    return inp1
def polar_nrz_l(inp):
    inp1 = list(inp)
    inp1 = ['-1' if i == '1' else '1' for i in inp1]
    return inp1
def polar_nrz_i(inp):
    inp2 = list(inp)
    lock = False
    for i in range(len(inp2)):
        if inp2[i] == '1' and not lock:
            lock = True
            continue
        if lock and inp2[i] == '1':
            if inp2[i - 1] == '0':
                inp2[i] = '1'
                continue
            else:
                inp2[i] = '0'
                continue
        if lock:
            inp2[i] = inp2[i - 1]
    inp2 = ['-1' if i == '0' else '1' for i in inp2]
    return inp2
def polar_rz(inp):
    inp1 = list(inp)
    inp1 = ['-1' if i == '0' else '1' for i in inp1]
    li = []
    for i in range(len(inp1)):
        li.append(inp1[i])
        li.append('0')
    return li
def biphase_manchester(inp):
    inp1 = list(inp)
    li, init = [], False
    for i in range(len(inp1)):
        if inp1[i] == '0':
            li.append('-1')
            if not init:
                li.append('-1')
                init = True
            li.append('1')
        elif inp1[i] == '1':
            li.append('1')
            li.append('-1')
    return li
def differential_manchester(inp):
    inp1 = list(inp)
    li, lock, pre = [], False, ''
    for i in range(len(inp1)):
        if inp1[i] == '0' and not lock:
            li.append('-1')
            li.append('-1')
            li.append('1')
            lock = True
            pre = 'inp'
        elif inp1[i] == '1' and not lock:
            li.append('1')
            li.append('1')
            li.append('-1')
            lock = True
            pre = 'Z'
        else:
            if inp1[i] == '0':
                if pre == 'inp':
                    li.append('-1')
                    li.append('1')
                else:
                    li.append('1')
                    li.append('-1')
            else:
                if pre == 'Z':
                    pre = 'inp'
                    li.append('-1')
                    li.append('1')
                else:
                    pre = 'Z'
                    li.append('1')
                    li.append('-1')

    return li
def ami(inp):
    inp1 = list(inp)
    inp1.insert(0, '0')
    lock = False
    for i in range(len(inp1)):
        if inp1[i] == '1' and not lock:
            lock = True
            continue
        elif lock and inp1[i] == '1':
            inp1[i] = '-1'
            lock = False
    return inp1
def plot(encoding_mode, inp):
    if encoding_mode == 'unipolar':
        plt.plot(unipolar(inp), color='red', drawstyle='steps-pre')
        plt.title("Unipolar ")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
    elif encoding_mode == 'polar_nrz_l':
        ls1 = list()
        for i in range(len(inp)):
            if (inp[i] == '0' or inp[i] == 0):
                ls1.append(1)
            else:
                ls1.append(-1)
        xs1 = np.repeat(range(len(inp)), 2)
        ys1 = np.repeat(ls1, 2)
        xs1 = xs1[1:]
        xs1 = np.append(xs1, (xs1[len(xs1) - 1] + 1))
        ys1 = ys1[:-1]
        ys1 = np.append(ys1, (ys1[len(ys1) - 1]))
        plt.step(xs1, ys1)
        plt.ylim(-2, 2)
        plt.title("Polar NRZ L")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
    elif encoding_mode == 'polar_nrz_i':
        Is = list()
        if (inp[0] == '0' or inp[0] == 0):
            Is.append(1)
        else:
            Is.append(-1)
        k = len(inp)
        i = 1
        while (i < k):
            if (int(inp[i]) == 0):
                Is.append(Is[i - 1])
            else:
                Is.append(-Is[i - 1])
            i = i + 1
        xs1 = np.repeat(range(len(inp)), 2)
        ys1 = np.repeat(Is, 2)
        xs1 = xs1[1:]
        xs1 = np.append(xs1, (xs1[len(xs1) - 1] + 1))
        ys1 = ys1[:-1]
        ys1 = np.append(ys1, (ys1[len(ys1) - 1]))
        plt.step(xs1, ys1)
        plt.ylim(-2, 2)
        plt.title("Polar NRZ I")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
    elif encoding_mode == 'polar_rz':
        plt.plot(polar_rz(inp), color='red', drawstyle='steps-pre')
        plt.title("Polar RZ")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
    elif encoding_mode == 'biphase_manchester':
        pm = list()
        for j in range(len(inp)):
            if (inp[j] == '0' or inp[j] == 0):
                pm.append(1)
                pm.append(-1)
            else:
                pm.append(-1)
                pm.append(1)
        xs1 = [x * 0.5 for x in range(0, (2 * len(inp)))]
        xs1 = np.repeat(xs1, 2)
        ys1 = np.repeat(pm, 2)
        xs1 = xs1[1:]
        xs1 = np.append(xs1, (xs1[len(xs1) - 1] + 0.5))
        ys1 = ys1[:-1]
        ys1 = np.append(ys1, (ys1[len(ys1) - 1]))
        plt.step(xs1, ys1)
        plt.ylim(-2, 2)
        plt.title("Manchester")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
    elif encoding_mode == 'differential_manchester':
        pdm = list()
        pdm.append(-1)
        pdm.append(1)
        i = 1
        k = len(inp)
        while (i < k):
            if (int(inp[i]) == 1):
                pdm.append(pdm[len(pdm) - 1])
                pdm.append(-pdm[len(pdm) - 1])
            else:
                pdm.append(-pdm[len(pdm) - 1])
                pdm.append(-pdm[len(pdm) - 1])
            i = i + 1
        print(pdm)
        xs1 = [x * 0.5 for x in range(0, (2 * len(inp)))]
        xs1 = np.repeat(xs1, 2)
        ys1 = np.repeat(pdm, 2)
        xs1 = xs1[1:]
        xs1 = np.append(xs1, (xs1[len(xs1) - 1] + 0.5))
        ys1 = ys1[:-1]
        ys1 = np.append(ys1, (ys1[len(ys1) - 1]))
        plt.step(xs1, ys1)
        plt.ylim(-2, 2)
        plt.title("Differential Manchester")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
    elif encoding_mode == 'ami':
        am = list()
        m = 1
        for i in range(len(inp)):
            if (int(inp[i]) == 0):
                am.append(0)
            else:
                if (m % 2 == 1):
                    am.append(1)
                else:
                    am.append(-1)
                m = m + 1
        xs = np.repeat(range(len(inp)), 2)
        ys = np.repeat(am, 2)
        xs = xs[1:]
        xs = np.append(xs, (xs[len(xs) - 1] + 1))
        ys = ys[:-1]
        ys = np.append(ys, (ys[len(ys) - 1]))
        plt.step(xs, ys)
        plt.ylim(-2, 2)
        plt.title("Alternative Mark Inversion")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
    else:
        print("Invalid encoding mode")
def process_input():
    inp = entry.get()
    if not inp:
        messagebox.showerror("Error", "Please enter a binary sequence.")
        return
    encoding_method = method_var.get()

    encoding_modes = {
        '1-unipolar': 'unipolar',
        '2-polar-nrz_l': 'polar_nrz_l',
        '3-polar-nrz_i': 'polar_nrz_i',
        '4-polar-rz': 'polar_rz',
        '5-biphase-manchester': 'biphase_manchester',
        '6-differential-manchester': 'differential_manchester',
        '7-ami': 'ami'
    }

    if encoding_method in encoding_modes:
        plot(encoding_modes[encoding_method], inp)
    else:
        messagebox.showerror("Error", "Invalid encoding method.")


root = Tk()
root.title("Binary Encoding")
frame = Frame(root)
frame.grid(padx=10, pady=10)
Label(frame, text="Enter the bits input").grid(row=0, column=0, padx=5, pady=5)
entry = Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)
Label(frame, text="Select Encoding Method:").grid(row=1, column=0, padx=5, pady=5)
encoding_modes = {
        '1-unipolar': 'unipolar',
        '2-polar-nrz_l': 'polar_nrz_l',
        '3-polar-nrz_i': 'polar_nrz_i',
        '4-polar-rz': 'polar_rz',
        '5-biphase-manchester': 'biphase_manchester',
        '6-differential-manchester': 'differential_manchester',
        '7-ami': 'ami'
    }
methods = list(encoding_modes.keys())
method_var = StringVar(frame)
method_var.set(methods[0])
method_menu = OptionMenu(frame, method_var, *methods)
method_menu.grid(row=1, column=1, padx=5, pady=5)
encode_button = Button(frame, text="Encode", command=process_input)
encode_button.grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()
