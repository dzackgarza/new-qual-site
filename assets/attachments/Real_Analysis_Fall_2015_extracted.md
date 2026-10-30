# Real Analysis Qualifying Exam, August 2015

<a id="real-analysis-qualifying-exam"></a>
## Instructions

Give clear reasoning. State clearly which theorem you are using. You should not cite anything else such as examples, exercises, or problems. Cross out the parts you do not want to be graded. Read through all the problems, do them in any order, the one you feel most confident about first. They are not in the order of difficulty.

<a id="problems-heading"></a>
## Problems

1. Let $f(x)=c_{0}+c_{1}x^{1}+c_{2}x^{2}+\ldots +c_{n}x^{n}$  with $n$  even and $c_{n}>0$ . Show that there is a number $x_{m}$  such that $f(x_{m})\leq f(x)$  for all $x\mathbb{\in R}$ .
2. Let $f$  be a real valued Lebesgue measurable function on $\mathbb{R}$ .

1. A simple function is one of the form

$$
s(x)=c_{1}\chi _{E_{1}}(x)+c_{2}\chi _{E_{2}}(x)+\cdots +c_{m}\chi _{E_{m}}(x),
$$

- where $c_{k}\mathbb{\in R}$  and $E_{k}$  are Lebesgue measurable sets. Show that there is a sequence of simple functions $s_{n}(x)$ , such that $lim_{n\rightarrow \infty }s_{n}(x)=f(x)$  for each $x$ . (Note: $\chi _{E}(x)=0$  if $x\in E$ , $\chi _{E}(x)=1$  if $x\notin E$ )

2. Show that there is a Borel measurable function $g$  such that $g(x)=f(x)$  almost everywhere.

3. Compute the following limit and justify your calculations:

$$
\lim_{n\to \infty }\int_{1}^{n}\frac{ne^{-x}}{1+nx^{2}}sin(x/n) \, dx
$$

4. Let $f(x)$  be real-valued, defined for $x\geq 1$ , satisfying $f(1)=1$  and

$$
f^{'}(x)=1/\left(x^{2}+f(x)^{2}\right)
$$

- Prove $lim_{x\rightarrow \infty }f(x)$  exists and $lim_{x\rightarrow \infty }f(x)\leq 1+\pi /4$ .

5. Let $f,g\in L^{1}\mathbb{(R)}$  and assume $f,g$  are Borel measurable.

1. Show that $f(x-y)g(y)$  is Borel measurable in $(x,y)$  and for almost every $x$ , $f(x-y)g(y)$  is integrable with respect to $y$  on $\mathbb{R}$ .
2. Define $f*g(x)=\int_{\mathbb{R}}^{​}f(x-y)g(y) \, dy$ . Show that $f*g\in L^{1}\mathbb{(R)}$  and

$$
\parallel f*g\parallel _{1}\leq \parallel f\parallel _{1}\parallel g\parallel _{1}.
$$

6. Let $f$  be a continuous real valued function on the interval $[0,1]$ . Show that

$$
sup\left\{\parallel fg\parallel _{1}:g\in L^{1}[0,1], \hspace{0.25em} \parallel g\parallel _{1}\leq 1\right\}=\parallel f\parallel _{\infty }.
$$