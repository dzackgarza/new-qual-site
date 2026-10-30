# Real Analysis Qualifying Examination — January 2016 — University of Georgia

**PRINT NAME:**

**SIGNATURE:**

Mathematics Department

The University of Georgia

Committee: Pete Clark (Chair), Jingzhi Tie and Shuzhou Wang

<a id="instructions"></a>
## Instructions

Give clear reasoning. State clearly which theorem you are using. You should not cite anything else such as examples, exercises, or problems. Cross out the parts you do not want to be graded. Read through all the problems, do them in any order, the one you feel most confident about first. They are not in the order of difficulty.

Notation: $\mathbb{R}$  is the set of real numbers; $m$  is the Lebesgue measure.

<table><thead><tr><th><p>Problem #</p></th><th><p>Points</p></th><th><p>Grade</p></th></tr></thead><tbody><tr><td><p>1</p></td><td><p>10</p></td><td></td></tr><tr><td><p>2</p></td><td><p>10</p></td><td></td></tr><tr><td><p>3</p></td><td><p>10</p></td><td></td></tr><tr><td><p>4</p></td><td><p>10</p></td><td></td></tr><tr><td><p>5</p></td><td><p>10</p></td><td></td></tr><tr><td><p>6</p></td><td><p>10</p></td><td></td></tr><tr><td><p>Total</p></td><td><p>60</p></td><td></td></tr></tbody></table>

<a id="committee-recommendation"></a>
## Committee Recommendation

Grader's Remarks

<a id="problems"></a>
## Problems

1. For $n\mathbb{\in N}$ , let $e_{n}=\left(1+\frac{1}{n}\right)^{n}$  and $E_{n}=\left(1+\frac{1}{n}\right)^{n+1}$ . It is obvious that $e_{n}<E_{n}$ . Prove Bernoulli's inequality:

$$
(1+x)^{n}\geq 1+nx \quad for -1<x<\infty and n\mathbb{\in N.}
$$

- Then use Bernoulli's inequality or any other method to show that

1. The sequence $e_{n}$  is increasing;
2. The sequence $E_{n}$  is decreasing;
3. $2\leq e_{n}<E_{n}\leq 4$ ;
4. $lim_{n\rightarrow \infty }e_{n}=lim_{n\rightarrow \infty }E_{n}$ .

2. Choose $0<\lambda <1$  and construct the Cantor set $C_{\lambda }$  as follows: Remove from $[0,1]$  its open middle part of length $\lambda$ ; we left with two intervals $I_{11}$  and $I_{12}$  of equal length. Remove from each of them their open middle parts of length $\lambda \, m(I_{11})$ , etc. and keep doing this ad infinitum. We are left with the set $C_{\lambda }$ . Prove that the set $C_{\lambda }$  has Lebesgue measure zero.
3. Let $f$  be a (Lebesgue) measurable function on $\mathbb{R}$  and $E$  be a measurable subset of $\mathbb{R}$  such that $0<A=\int_{E}^{​}f(x) \, dx<\infty$ . Show that for every number $0<t<1$ , there exists a measurable subset $E_{t}\subset E$  such that $\int_{E_{t}}^{​}f(x) \, dx=tA$ .
4. Let $E$  be a Lebesgue measurable set in $\mathbb{R}$  with $m(E)<\infty$ . Define

$$
f(x)=m(E\cap (E+x))
$$

- Show that (a) $f$  is in $L^{1}\mathbb{(R)}$ ; (b) $f$  is uniformly continuous; (c) $lim_{|x|\rightarrow \infty }f(x)=0$ .
- Hint You may use this identity of characteristic functions: $\chi _{E\cap (E+x)}(y)=\chi _{E}(y)\chi _{E}(y-x)$ .

5. Let $(X\mathscr{,M,}\mu )$  be a measured space. For $f\in L^{1}(\mu )$  and $\lambda >0$ , define

$$
\phi (\lambda )=\mu (\{x\in X\mid f(x)>\lambda \}) \quad and \quad \psi (\lambda )=\mu (\{x\in X\mid f(x)<-\lambda \}).
$$

- Show that the function $\phi$  and $\psi$  are Borel measurable and that

$$
\int_{X}^{​}|f| \, d\mu =\int_{0}^{\infty }[\phi (\lambda )+\psi (\lambda )] \, d\lambda .
$$

6. Compute the following without using the Riesz representation theorem:

$$
sup\left\{\left|\int_{0}^{1}f(x)e^{x} \, dx\right|:f\in L^{2}([0,1],m), \hspace{0.25em} \parallel f\parallel _{2}\leq 1\right\}.
$$