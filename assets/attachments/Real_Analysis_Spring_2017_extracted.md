# Real Analysis Qualifying Exam — January 2017

<a id="real-analysis-qualifying-exam"></a>
## Instructions

Give clear reasoning. State clearly which theorem you are using. You should not cite anything else such as examples, exercises, or problems. Cross out the parts you do not want to be graded. Problems are not in the order of difficulty.

Notation: $m$  denotes the Lebesgue measure on the set $\mathbb{R}$  of reals.

<a id="problems"></a>
## Problems

1. Let $K$  be the set of numbers in $[0,1]$  whose decimal expansions do not use the digit $4$  (we use the convention that when a decimal number ends with $4$  but all other digits are different from $4$ , we replace the digit $4$  with $399\ldots$ . For example, $0.8754=0.8753999\ldots$ .) Show that $K$  is a compact, nowhere dense set without isolated points, and find the Lebesgue measure $m(K)$ .
2. (a) Let $\mu$  be a measure on a measurable space $(X\mathscr{,M)}$  and $f$  a positive measurable function. Let $\lambda$  be the measure defined by

$$
\lambda (E):=\int_{E}^{​}f \, d\mu , \quad \quad E\mathscr{\in M.}
$$

- Show that for any positive measurable function $g$ ,

$$
\int_{X}^{​}g \, d\lambda =\int_{X}^{​}fg \, d\mu .
$$

- (b) Let $E\mathbb{\subset R}$  be a Lebesgue measurable set such that $\int_{E}^{​}x^{2} \, dm=0$ . Show that $m(E)=0$ .

3. Let $f_{n}(x)=ae^{-nax}-be^{-nbx}$  where $0<a<b$ . Show that

1. $\sum_{n=1}^{\infty }|f_{n}|$  is not in $L^{1}([0,\infty ),m)$ . Hint: $f_{n}(x)$  has a root $x_{n}$ .
2. $\sum_{n=1}^{\infty }f_{n}$  is in $L^{1}([0,\infty ),m)$  and $\int_{0}^{\infty }\sum_{n=1}^{\infty }f_{n}(x) \, dm=ln\frac{b}{a}$ .

4. Let $f(x,y)$  be the function on $[-1,1]\times [-1,1]$  defined by $f(x,y)=\frac{xy}{(x^{2}+y^{2})^{2}}$  if $(x,y)\ne (0,0)$  and $f(0,0)=0$ . Determine if $f$  is integrable and justify your assertion.
5. Let $f,g\in L^{2}\mathbb{(R)}$ . Prove that the formula

$$
h(x):=\int_{-\infty }^{\infty }f(t)g(x-t) \, dt
$$

- defines a uniformly continuous function $h$  on $\mathbb{R}$ .

6. Show that the space $C^{1}([a,b])$  of continuously differentiable functions $f$  on $[a,b]$  is a Banach space under the norm $\parallel f\parallel :=sup_{x\in [a,b]}|f(x)|+sup_{x\in [a,b]}|f^{'}(x)|$ . (No need to show this is a norm.)