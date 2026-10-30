# Real Analysis Qualifying Exam, Fall 2021

<a id="real-analysis-qualifying-exam-fall-2021"></a>
## Problems

1. Let $\left\{x_{n}\right\}_{n=1}^{\infty }$  be a sequence of real numbers such that $x_{1}>0$  and

$$
x_{n+1}=1-\left(2+x_{n}\right)^{-1}=\frac{1+x_{n}}{2+x_{n}}.
$$

- Prove that the sequence $\left\{x_{n}\right\}$  converges, and find its limit.

1. Let $F\mathbb{\subset R}$  be closed, and define

$$
\delta _{F}(y):=\underset{x\in F}{inf}|x-y|.
$$

- For $y\notin F$ , show that

$$
\int_{F}^{​}|x-y|^{-2} \, dx\leq \frac{2}{\delta _{F}(y)}.
$$

2. Let $F\mathbb{\subset R}$  be a closed set whose complement has finite measure, i.e. $m\mathbb{(R\smallsetminus}F)<\infty$ . Define the function

$$
I(x):=\int_{\mathbb{R}}^{​}\frac{\delta _{F}(y)}{|x-y|^{2}} \, dy.
$$

- Prove that $I(x)=\infty$  if $x\notin F$ , however $I(x)<\infty$  for almost every $x\in F$ . (Hint: investigate $\int_{F}^{​}I(x) \, dx$ .)

2. Recall that a set $E\subset \mathbb{R}^{d}$  is measurable if for every $\epsilon >0$  there is an open set $U\subset \mathbb{R}^{d}$  such that $m^{*}(U\smallsetminus E)<\epsilon$ .

1. Prove that if $E$  is measurable then for all $\epsilon >0$  there exists an elementary set $F$ , such that $m(E\Delta F)<\epsilon$ . Here $m(E)$  denotes the Lebesgue measure of $E$ , a set $F$  is called elementary if it is a finite union of rectangles and $E\Delta F$  denotes the symmetric difference of the sets $E$  and $F$ .
2. Let $E\mathbb{\subset R}$  be a measurable set, such that $0<m(E)<\infty$ .

- Use part (a) to show that,

$$
\lim_{n\to \infty }\int_{E}^{​}sin(nt) \, dt=0
$$

3. Let $f$  be a measurable function on $\mathbb{R}$ . Show that the graph of $f$  has measure zero in $\mathbb{R}^{2}$ .
4. Consider the Hilbert space $\mathscr{H=}L^{2}([0,1])$ .

1. Prove that if $E\mathscr{\subset H}$  is closed and convex then $E$  contains an element of smallest norm. Hint: Show that if $\left\|f_{n}\right\|_{2}\rightarrow min\left\{\left\|f\right\|_{2}:f\in E\right\}$  then $\left\{f_{n}\right\}$  is a Cauchy sequence.
2. Construct a non-empty closed subset $E\mathscr{\subset H}$  which does not contain an element of smallest norm.