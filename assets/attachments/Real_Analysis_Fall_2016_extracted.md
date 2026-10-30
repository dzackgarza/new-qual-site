# Real Analysis Qualifying Exam, August 2016

<a id="real-analysis-qualifying-exam"></a>
## Instructions

Give clear reasoning. State clearly which theorem you are using. You should not cite anything else such as examples, exercises, or problems. Cross out the parts you do not want to be graded. Read through all the problems, do them in any order, the one you feel most confident about first. They are not in the order of difficulty.

Notation: $\mathbb{R}$  is the set of real numbers; $dx$  is the Lebesgue measure.

<a id="problems"></a>
## Problems

1. Prove that the series

$$
\sum_{n=1}^{\infty }\frac{1}{n^{x}}
$$

- converges to a differentiable function on $(1,\infty )$  and that

$$
\left(\sum_{n=1}^{\infty }\frac{1}{n^{x}}\right)^{'}=\sum_{n=1}^{\infty }\left(\frac{1}{n^{x}}\right)^{'},
$$

- where $'$  means derivative with respect to $x$ . (Recall that $\left(n^{-x}\right)^{'}=-n^{-x}lnn$ .)

2. Let $f$  and $g$  be real valued measurable functions on $[a,b]$  with

$$
\int_{a}^{b}f(x) \, dx=\int_{a}^{b}g(x) \, dx.
$$

- Show that either $f(x)=g(x)$  a.e., or there exists measurable subset $E$  of $[a,b]$  such that

$$
\int_{E}^{​}f(x) \, dx>\int_{E}^{​}g(x) \, dx.
$$

3. Let $f\in L^{1}\mathbb{(R)}$ . Show that

$$
\lim_{x\to 0}\int_{\mathbb{R}}^{​}|f(y-x)-f(y)| \, dy=0.
$$

4. Let $(X\mathscr{,M,}\mu )$  be a measure space and suppose that $\{E_{n}\}$  is a sequence from $\mathscr{M}$  with the property that

$$
\lim_{n\to \infty }\mu (X \textbackslash E_{n})=0.
$$

- Let $G$  be the set of $x$ 's that belong to only finitely many of the sets $E_{n}$ . Show that $G\mathscr{\in M}$  and $\mu (G)=0$ .

5. Let $\phi \in L^{\infty }\mathbb{(R)}$  (the measure on $\mathbb{R}$  is the usual Lebesgue measure). Show that

$$
\lim_{n\to \infty }\left(\int_{\mathbb{R}}^{​}\frac{|\phi (x)|^{n}}{1+x^{2}} \, dx\right)^{\frac{1}{n}}
$$

- exists and equals to $\parallel \phi \parallel _{\infty }$ .

6. Let $f$  and $g$  belong to $L^{2}\mathbb{(R)}$ . Show that

$$
\lim_{n\to \infty }\int_{\mathbb{R}}^{​}f(x)g(x+n) \, dx=0.
$$