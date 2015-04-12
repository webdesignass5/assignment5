from flask import Flask, render_template, request

app = Flask(__name__)
import os


@app.route('/')
def index1():
    return render_template('home.html')


@app.route('/home.html')
def index2():
    return render_template('home.html')


@app.route('/intro1.html')
def index3():
    return render_template('intro1.html')


@app.route('/intro2.html')
def index4():
    return render_template('intro2.html')


@app.route('/intro3.html')
def index5():
    return render_template('intro3.html')


@app.route('/avg.html',  methods=['GET', 'POST'])
def index6():
    s = None
    p1 = None
    #p2 = None
    #p3 = None
    if request.method == 'POST' and 'n1' in request.form:
        p1 = [eval(request.form['n1'])]
        p1 = list(p1)
        x = len(p1[0])
        y = reduce(lambda x, y: x + y, p1[0])
        x = float(x)
        s = y / x
        s = round(s, 3)
    return render_template('avg.html', s=s)


@app.route('/integrate.html',  methods=['GET', 'POST'])
def index7():
    a = None
    b = None
    n = None
    fn = None
    sol = None
    k = None
    if request.method == 'POST' and 'a' in request.form and 'b' in request.form and 'n' in request.form and 'fn' in request.form:
        a = request.form['a']
        b = request.form['b']
        n = request.form['n']
        # fn = request.form['fn']
        fn = lambda x: eval(request.form['fn'])
        a = float(a)
        b = float(b)
        n = float(n)
        k = (b - a) / n
        sol = fn(a)
        q = []
        n = int(n)
        for i in range(1, n):
            i = float(i)
            q.append(i)
        for i in q:
            sol += 2 * fn(a + (i * k))
        sol = sol + fn(b)
        a = int(a)
        b = int(b)
        sol = (sol * k) / 2
        import matplotlib.pyplot as pt  # import plotting library
        from numpy import arange

        fig = pt.figure()

        x = [i for i in arange(a, b, (b - a) / (n * 1000.0))]  # list of values between a and b
        x = x + [b]
        y = [i for i in arange(a, b, (b - a) / (n * 1.0))]  # list of values of x
        y = y + [b]
        z = [fn(i) for i in x]  # list of function values
        pt.plot(x, z)  # plotting the curve
        for i in range(n + 1):
            pt.plot([y[i], y[i]], [0, fn(y[i])])  # parallel sides of the trapezium
        for i in range(n):
            pt.plot([y[i], y[i + 1]], [fn(y[i]), fn(y[i + 1])])  # non-parallel sides of trapezium
        # pt.show()  #output
        pt.axvline(0, color="k")
        pt.axhline(0, color="k")
        if os.path.exists("C:\\Users\\INCREDIBLE VIVEK\\PycharmProjects\\web design\\static\\graph.png"):
            os.remove("C:\\Users\\INCREDIBLE VIVEK\\PycharmProjects\\web design\\static\\graph.png")
            pt.savefig("C:\\Users\\INCREDIBLE VIVEK\\PycharmProjects\\web design\\static\\graph.png", dpi=fig.dpi)
        else:
            pt.savefig("C:\\Users\\INCREDIBLE VIVEK\\PycharmProjects\\web design\\static\\graph.png", format="png",
                       dpi=fig.dpi)
    return render_template('integrate.html', sol=sol)

if __name__ == '__main__':
    app.run(debug=True)



