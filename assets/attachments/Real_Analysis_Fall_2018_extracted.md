# Real Analysis Qualifying Exam, Fall 2018

<a id="real-analysis-qualifying-exam-fall-2018"></a>
## Instructions

Use a separate sheet of paper for each problem, and write your name on each sheet. Give clear reasoning. State clearly which theorems you are using. You should not cite anything else such as examples, exercises, or problems. Cross out the parts you do not want to be graded. $m$  denotes Lebesgue measure.

<a id="problems"></a>
## Problems

1. Let $f(x)=\frac{1}{x}$ . Show that $f(x)$  is uniformly continuous on $(1,\infty )$  but not on $(0,\infty )$ .
2. Let $E\mathbb{\subset R}$  be a Lebesgue measurable set. Show that there is a Borel set $B\subset E$ , such that $m(E \textbackslash B)=0$ .
3. Suppose $f(x)$  and $xf(x)$  are integrable on $\mathbb{R}$ . Define $F$  by

$$
F(t):=\int_{-\infty }^{\infty }f(x)cos(xt) \, dx
$$

- Show that

$$
F^{'}(t)=-\int_{-\infty }^{\infty }xf(x)sin(xt) \, dx.
$$

4. Let $f\in L^{1}[0,1]$ . Prove that

$$
\lim_{n\to \infty }\int_{0}^{1}f(x)|sinnx| \, dx=\frac{2}{\pi }\int_{0}^{1}f(x) \, dx.
$$

- Hint: begin with the case in which $f$  is the characteristic function of an interval.

5. Let $f\geq 0$  be a Lebesgue measurable function on $\mathbb{R}$ . Show that

$$
\int_{\mathbb{R}}^{​}f=\int_{0}^{\infty }m(\{x:f(x)>t\}) \, dt.
$$

6. Compute the following limit and justify your calculations:

$$
\lim_{n\to \infty }\int_{1}^{n}\frac{dx}{\left(1+\frac{x}{n}\right)^{n}\sqrt[n]{x}}
$$