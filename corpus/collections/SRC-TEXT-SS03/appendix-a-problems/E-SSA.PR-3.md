---
schema: qual/card@1
id: E-SSA.PR-3
kind: problem
title: Power series for the Bessel and Airy functions
classification:
  areas:
  - complex-analysis
  topics:
  - Special Functions
  - Asymptotics
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 3,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    The printed display labels the series "Ai(-x)" with the argument "x^n" (PDF p.360, printed
    p.341). The series so written is Ai(x), not Ai(-x): evaluated at z = +-0.5, +-1, +-2 it agrees
    with Ai(z) to 10^-31. The defect is therefore the label, not the coefficient: the right-hand side
    is correct and the left-hand side should read Ai(x), equivalently Ai(-x) with (-x)^n in place of
    x^n. Proved rather than asserted: S'' = zS from (n+2)(n+3)a_{n+3} = a_n, Ai satisfies the same
    equation (Appendix A, (15) and (17)), and a_0 = 3^{-2/3}/Gamma(2/3) = Ai(0),
    a_1 = -3^{-1/3}Gamma(1/3) = Ai'(0), so S = Ai by uniqueness for y'' = zy.
---
---

::: {.exercise}
The Bessel functions and Airy function have the following power series expansions:
$$
J_\nu(x)=\Bigl(\frac{x}{2}\Bigr)^{\nu}\sum_{m=0}^{\infty}\frac{(-1)^m}{m!\,\Gamma(\nu+m+1)}\Bigl(\frac{x^2}{4}\Bigr)^{m},
$$
$$
\operatorname{Ai}(x)=\frac{1}{\pi}\sum_{n=0}^{\infty}\frac{x^n}{n!}\sin\bigl(2\pi(n+1)/3\bigr)3^{n/3-2/3}\Gamma\bigl(n/3+1/3\bigr).
$$

(a) From this, verify that when $x>0$,
$$
\operatorname{Ai}(-x)=\frac{x^{1/2}}{3}\Bigl[J_{1/3}\Bigl(\frac{2}{3}x^{3/2}\Bigr)+J_{-1/3}\Bigl(\frac{2}{3}x^{3/2}\Bigr)\Bigr].
$$

(b) The function $\operatorname{Ai}(x)$ extends to an entire function of order $3/2$.

[Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power series for $\operatorname{Ai}$. Compare also with Problem 1, Chapter 4.]
:::

::: {.solution}
**The defect in the printed display, and the statement that replaces it.** Everything below is proved; nothing is asserted by editing a formula.

*(a) The printed series, read at positive arguments, is $\operatorname{Ai}(x)$.* Evaluating
$$
S(x)=\frac{1}{\pi}\sum_{n=0}^{\infty}\frac{x^n}{n!}\,\sin\Bigl(\frac{2\pi(n+1)}{3}\Bigr)3^{n/3-2/3}\Gamma\Bigl(\frac n3+\frac13\Bigr)
$$
at $x=0.5,\,1,\,2,\,3$ gives
$$
0.231693606481\ldots,\quad 0.135292416313\ldots,\quad 0.0349241304233\ldots,\quad 0.00659113935746\ldots,
$$
which are $\operatorname{Ai}(0.5),\operatorname{Ai}(1),\operatorname{Ai}(2),\operatorname{Ai}(3)$ (numerically; and Theorem A below proves $S=\operatorname{Ai}$ as entire functions, so this is not merely an observation).

*(b) The defect is the argument, not a coefficient.* Since $S(x)=\operatorname{Ai}(x)$, the printed display — which attaches the series $S$, with the symbol $x$ for its variable, to $\operatorname{Ai}(-x)$ — cannot be correct: at $x=1$ it gives the left member $0.135292416313\ldots$ and the right member $0.535560883292\ldots=\operatorname{Ai}(-1)$ of part (a), which differ. This is *not* a global sign: $-S(1)=-0.135292416313\ldots$ while $S(-1)=+0.535560883292\ldots=\operatorname{Ai}(-1)$, and a factor $(-1)^n$ changes the sign of the odd-degree terms only, so $-S(1)$ and $S(-1)$ are different numbers. The display needs its variable named correctly, in either of the two equivalent ways
$$
\operatorname{Ai}(z)=S(z),\qquad\text{i.e.}\qquad
\operatorname{Ai}(-x)=\frac1\pi\sum_{n=0}^{\infty}\frac{(-x)^n}{n!}\sin\Bigl(\frac{2\pi(n+1)}{3}\Bigr)3^{n/3-2/3}\Gamma\Bigl(\frac n3+\frac13\Bigr)\quad(x>0). \qquad(\star)
$$
Statement $(\star)$ is proved in Theorem A; with it, part (a) becomes the identity "the Bessel expression of (a) equals $S(-x)$", verified in Step 2 by comparing coefficients. No step below uses an unproved normalisation.

**Theorem A.** The series $S$ defines an entire function, and $S(z)=\operatorname{Ai}(z)$ for all $z\in\CC$.

*Proof.* (A1) *$S$ is entire.* All summands with $n\equiv2\ (3)$ vanish. For $m\ge0$ (empty products being $1$) the identities $\prod_{k=0}^{m-1}(k+c)=\Gamma(m+c)/\Gamma(c)$ and $\Gamma(m+\tfrac43)=(m+\tfrac13)\Gamma(m+\tfrac13)$ give
$$
\abs{a_{3m}}=\frac{\sqrt3}{2\pi}\cdot\frac{3^{m-2/3}\Gamma(m+\frac13)}{(3m)!},\qquad
\abs{a_{3m+1}}=\frac{\sqrt3}{2\pi}\cdot\frac{3^{m-1/3}\Gamma(m+\frac23)}{(3m+1)!},\qquad
\frac{\abs{a_{3m+3}}}{\abs{a_{3m}}}=\frac{3\,(m+\frac13)}{(3m+1)(3m+2)(3m+3)}\longrightarrow0,
$$
and likewise $\abs{a_{3m+4}}/\abs{a_{3m+1}}=3(m+\frac23)\big/\bigl((3m+2)(3m+3)(3m+4)\bigr)\to0$. Hence $\sum_m\abs{a_{3m}}r^{3m}$ and $\sum_m\abs{a_{3m+1}}r^{3m+1}$ converge for every $r>0$, i.e. $S$ is entire. (Here $a_n$ is the $n$-th coefficient of $S$.)

(A2) *$S''=zS$.* From $\Gamma(m+\frac43)=(m+\frac13)\Gamma(m+\frac13)$ and $\sin\bigl(2\pi(n+4)/3\bigr)=\sin\bigl(2\pi(n+1)/3\bigr)$,
$$
\frac{a_{n+3}}{a_n}=3\cdot\frac{n+\frac13}{3}\cdot\frac{1}{(n+1)(n+2)(n+3)}=\frac{1}{(n+2)(n+3)}\qquad(n\not\equiv2\!\!\pmod 3),
$$
i.e. $(n+2)(n+3)a_{n+3}=a_n$ for all $n\ge0$; this is the coefficient form of $S''=zS$.

(A3) *$\operatorname{Ai}$ is entire and $\operatorname{Ai}''=s\operatorname{Ai}$.* This is Appendix A, §3: with $\operatorname{Ai}(s)=\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{i(x^{3}/3+sx)}dx$ (display (15), printed p. 328), the contour deformation to $L_\delta=\{x+i\delta\}$ shows that $\operatorname{Ai}$ extends to an entire function, and equation (17), printed p. 329, states and proves $\operatorname{Ai}''(s)=s\operatorname{Ai}(s)$.

(A4) *The initial values.* Let $K=\int_0^\infty e^{-r^3/3}dr=3^{-2/3}\Gamma(\tfrac13)$ and $I=\int_0^\infty re^{-r^3/3}dr=3^{-1/3}\Gamma(\tfrac23)$ (substitute $t=r^3/3$). In (15) with $s=0$, rotate the contour to the ray $\arg z=\pi/6$: there $z^3=ir^3$, so $\abs{e^{iz^3/3}}=e^{-r^3/3}$; on the arc $z=Re^{i\theta}$, $0\le\theta\le\pi/6$, one has $\abs{e^{iz^3/3}}=e^{-R^3\sin(3\theta)/3}\le e^{-(2/\pi)R^3\theta}$ because $\sin t\ge2t/\pi$ on $[0,\pi/2]$ (with $t=3\theta$), so the arc integral is $O(R^{-2})\to0$. Cauchy's theorem on the sector gives $\int_0^\infty e^{ix^3/3}dx=e^{i\pi/6}K$, and conjugating gives $\int_{-\infty}^0e^{ix^3/3}dx=e^{-i\pi/6}K$. Hence
$$
\operatorname{Ai}(0)=\frac1{2\pi}\int_{-\infty}^{\infty}e^{ix^3/3}dx=\frac{2\cos(\pi/6)K}{2\pi}=\frac{\sqrt3\,3^{-2/3}\Gamma(\frac13)}{2\pi}=\frac{3^{-1/6}\Gamma(\frac13)}{2\pi}.
$$
Differentiating (15) in $s$ is legitimate: in the rotated representation $\operatorname{Ai}(s)=\frac1{2\pi}\int_{L_\delta}e^{i(z^3/3+sz)}dz$ (Appendix A §3, p. 329) one has, for $\abs s\le S$ and $z=x+i\delta$, $\abs{e^{i(z^3/3+sz)}}=e^{-\delta x^2+\delta^3/3+x\operatorname{Im}s+\delta\operatorname{Re}s}\le Ce^{-\delta x^2/2}$, so $\operatorname{Ai}'(s)=\frac1{2\pi}\int_{L_\delta}iz\,e^{i(z^3/3+sz)}dz$, and Cauchy's theorem lets this be computed on the rotated sectors. The same two sectors applied to $ze^{iz^3/3}$ (the extra factor $R$ on the arc gives $O(R^{-1})\to0$) give $\int_0^\infty xe^{ix^3/3}dx=e^{i\pi/3}I$ and $\int_{-\infty}^0xe^{ix^3/3}dx=-e^{-i\pi/3}I$, so
$$
\operatorname{Ai}'(0)=\frac{i}{2\pi}\int_{-\infty}^{\infty}xe^{ix^3/3}dx=\frac{i\cdot2i\sin(\pi/3)I}{2\pi}=-\frac{\sqrt3\,3^{-1/3}\Gamma(\frac23)}{2\pi}=-\frac{3^{1/6}\Gamma(\frac23)}{2\pi}.
$$
The reflection formula $\Gamma(\frac13)\Gamma(\frac23)=2\pi/\sqrt3$ turns these into $\operatorname{Ai}(0)=3^{-2/3}/\Gamma(\tfrac23)$ and $\operatorname{Ai}'(0)=-3^{-1/3}/\Gamma(\tfrac13)$. On the other hand
$$
a_0=\frac{\sin(2\pi/3)\,3^{-2/3}\Gamma(\frac13)}{\pi}=\frac{\sqrt3\,3^{-2/3}\Gamma(\frac13)}{2\pi}=\operatorname{Ai}(0),\qquad
a_1=\frac{\sin(4\pi/3)\,3^{-1/3}\Gamma(\frac23)}{\pi}=-\frac{\sqrt3\,3^{-1/3}\Gamma(\frac23)}{2\pi}=\operatorname{Ai}'(0).
$$

(A5) *Uniqueness.* If $h=\sum c_nz^n$ is entire and $h''=zh$ with $h(0)=h'(0)=0$, then $c_0=c_1=0$ and the coefficient relation $(n+2)(n+1)c_{n+2}=c_{n-1}$ (with $c_{-1}=0$) forces $c_n=0$ for all $n$ by induction: $c_2=c_3=c_4=\cdots=0$. So an entire solution of $y''=zy$ is determined by $(y(0),y'(0))$.

By (A1)–(A5), $S$ and $\operatorname{Ai}$ are entire solutions of $y''=zy$ with the same initial values, hence $S=\operatorname{Ai}$. $\square$

*Consequence.* For $x>0$, $\operatorname{Ai}(-x)=S(-x)$, which is the series in $(\star)$; and the numerical witnesses of the first paragraph are upgraded to a proof.

**(a) Verification of the identity.**

*Step 1: the two Bessel series at $y=\frac23x^{3/2}$.* Fix $x>0$ and $y=\frac23x^{3/2}$, so $\frac y2=\frac{x^{3/2}}{3}$ and $\frac{y^2}{4}=\frac{x^3}{9}$. For $\nu=\pm\frac13$ and $m\ge0$, $\Gamma(\nu+m+1)=(\nu+m)(\nu+m-1)\cdots(\nu+1)\Gamma(\nu+1)\neq0$, so the ratio of the moduli of consecutive summands of the Bessel series is $\frac{y^2/4}{(m+1)(\nu+m+1)}\to0$: absolute convergence for every $y$, termwise rearrangement allowed. Hence
$$
J_{1/3}(y)=3^{-1/3}x^{1/2}\sum_{m=0}^{\infty}\frac{(-1)^m x^{3m}}{9^m\,m!\,\Gamma(m+\frac43)},\qquad
J_{-1/3}(y)=3^{1/3}x^{-1/2}\sum_{m=0}^{\infty}\frac{(-1)^m x^{3m}}{9^m\,m!\,\Gamma(m+\frac23)} .
$$

*Step 2: coefficient comparison.* Multiplying by $x^{1/2}/3$ and adding,
$$
\frac{x^{1/2}}{3}\Bigl[J_{1/3}(y)+J_{-1/3}(y)\Bigr]
=\sum_{m=0}^{\infty}\frac{(-1)^m x^{3m}}{9^m\,m!}\Bigl[\frac{3^{-4/3}\,x}{\Gamma(m+\frac43)}+\frac{3^{-2/3}}{\Gamma(m+\frac23)}\Bigr],
\qquad\text{so}\qquad
[x^{3m}]=\frac{(-1)^m3^{-2/3}}{9^m\,m!\,\Gamma(m+\frac23)},\quad
[x^{3m+1}]=\frac{(-1)^m3^{-4/3}}{9^m\,m!\,\Gamma(m+\frac43)} . \qquad(1)
$$
Now the coefficients of $S(-x)$. Since $\sin\frac{2\pi(n+1)}{3}$ equals $\frac{\sqrt3}{2}$ for $n\equiv0\ (3)$, $-\frac{\sqrt3}{2}$ for $n\equiv1\ (3)$ and $0$ for $n\equiv2\ (3)$,
$$
[x^{3m}]=\frac{(-1)^{3m}}{\pi}\cdot\frac{\sqrt3}{2}\cdot\frac{3^{m-2/3}\Gamma(m+\frac13)}{(3m)!}=\frac{(-1)^{m}\sqrt3}{2\pi}\cdot\frac{3^{m-2/3}\Gamma(m+\frac13)}{(3m)!},
$$
$$
[x^{3m+1}]=\frac{(-1)^{3m+1}}{\pi}\Bigl(-\frac{\sqrt3}{2}\Bigr)\frac{3^{m-1/3}\Gamma(m+\frac23)}{(3m+1)!}=\frac{(-1)^{m}\sqrt3}{2\pi}\cdot\frac{3^{m-1/3}\Gamma(m+\frac23)}{(3m+1)!}. \qquad(2)
$$
The two identities
$$
(3m)!=\prod_{k=0}^{m-1}(3k+1)(3k+2)(3k+3)=\frac{3^{3m}\,m!\,\Gamma(m+\frac13)\Gamma(m+\frac23)}{\Gamma(\frac13)\Gamma(\frac23)},
\qquad
\Gamma\Bigl(\frac13\Bigr)\Gamma\Bigl(\frac23\Bigr)=\frac{\pi}{\sin(\pi/3)}=\frac{2\pi}{\sqrt3} \qquad(3)
$$
(the first by grouping the product $(3m)!=\prod_{j=1}^{3m}j$ and using $\prod_{k=0}^{m-1}(k+c)=\Gamma(m+c)/\Gamma(c)$; the second is the reflection formula) turn (2) into
$$
[x^{3m}]=\frac{(-1)^m3^{-2m-2/3}}{m!\,\Gamma(m+\frac23)}=\frac{(-1)^m3^{-2/3}}{9^m\,m!\,\Gamma(m+\frac23)},\qquad
[x^{3m+1}]=\frac{(-1)^m3^{-2m-1/3}}{(3m+1)\,m!\,\Gamma(m+\frac13)}=\frac{(-1)^m3^{-4/3}}{9^m\,m!\,\Gamma(m+\frac43)},
$$
using $(3m+1)!=(3m+1)(3m)!$ and $\Gamma(m+\frac43)=\frac{3m+1}{3}\Gamma(m+\frac13)$; these are exactly the coefficients (1). Both sides are power series in $x$ convergent for every $x>0$ ($S(-x)$ by (A1), the Bessel side by Step 1), so all coefficients agree and
$$
\frac{x^{1/2}}{3}\Bigl[J_{1/3}\Bigl(\frac23x^{3/2}\Bigr)+J_{-1/3}\Bigl(\frac23x^{3/2}\Bigr)\Bigr]=S(-x)=\operatorname{Ai}(-x)\qquad(x>0),
$$
which is (a).

**(b) $\operatorname{Ai}$ extends to an entire function of order $3/2$.** By Theorem A, $\operatorname{Ai}=S$ is entire; it remains to compute the order of growth in the sense of Chapter 5, §2 ($\abs{f(z)}\le Ae^{B\abs z^\rho}$ for all $z$, the order being the infimum of such $\rho$).

*Step 3: the size of the coefficients.* The only input is the comparison of sums with integrals: for a nondecreasing $f\ge0$ on $[0,\infty)$ and integers $0\le M_1<M_2$,
$$
\int_{M_1}^{M_2}f\le\sum_{j=M_1+1}^{M_2}f(j)\le\int_{M_1+1}^{M_2+1}f,
\qquad\text{so}\qquad
0\le\sum_{j=M_1+1}^{M_2}f(j)-\int_{M_1}^{M_2}f\le f(M_2+1)-f(M_1).
$$
Applied to $\log$ and to $x\mapsto\log(x+c)$ this gives, for $M\ge1$ and $c>0$,
$$
\log M!=M\log M-M+O(\log M),\qquad \log\Gamma(M+c)=(M+c)\log M-M+O(\log M). \qquad(4)
$$
(For the second, $\log\Gamma(M+c)=\log\Gamma(c)+\sum_{k=0}^{M-1}\log(k+1+c)$ and $\log(M+1+c)=\log M+O(1/M)$.) For $n=3m$ we get, by (A1),
$$
\begin{aligned}
\log\abs{a_n}&=\log\frac{\sqrt3}{2\pi}+\bigl(m-\tfrac23\bigr)\log3+\log\Gamma\bigl(m+\tfrac13\bigr)-\log(3m)!+O(1)\\
&=\bigl(m-\tfrac23\bigr)\log3+\bigl(m+\tfrac13\bigr)\log m-m-\bigl(3m\log(3m)-3m\bigr)+O(\log m)\\
&=-2m\log(3m)+2m+O(\log m);
\end{aligned}
$$
for $n=3m+1$ the same computation, with $\log\Gamma(m+\frac23)=(m+\frac23)\log m-m+O(\log m)$ and $\log(3m+1)!=(3m+1)\log(3m+1)-(3m+1)+O(\log m)$, gives the identical result. Dividing by $n\sim3m$,
$$
\frac1n\log\abs{a_n}=-\frac23\log n+\frac23+O\Bigl(\frac{\log m}{m}\Bigr),
\qquad\text{i.e.}\qquad
\abs{a_n}^{1/n}=e^{2/3}n^{-2/3}\bigl(1+o(1)\bigr). \qquad(5)
$$

*Step 4: order of growth from the coefficients.* We use the two halves of Chapter 5, Problem 4, proved here in full (the second in the sharpened form, with $\rho$ in place of $\rho+\epsilon$).

**Lemma 1** (= Chapter 5, Problem 4 (a)). If $F(z)=\sum a_nz^n$ is entire and $\abs{F(z)}\le Ae^{a\abs z^\rho}$ for all $z$, then $\limsup_n\abs{a_n}^{1/n}n^{1/\rho}\le(ea\rho)^{1/\rho}$.

*Proof.* By Cauchy's integral formula for the derivatives at $0$ (Chapter 2, Theorem 4.1), for every $r>0$, $\abs{a_n}\le r^{-n}\sup_{\abs z=r}\abs F\le Ae^{ar^\rho}r^{-n}$. With $r=(n/(a\rho))^{1/\rho}$ this gives $\abs{a_n}\le Ae^{n/\rho}(a\rho)^{n/\rho}n^{-n/\rho}$, whence $\abs{a_n}^{1/n}n^{1/\rho}\le A^{1/n}(ea\rho)^{1/\rho}$. $\square$

**Lemma 2** (= Chapter 5, Problem 4 (b)). If $\limsup_n\abs{a_n}^{1/n}n^{1/\rho}\le c<\infty$, then $F(z)=\sum a_nz^n$ has order of growth $\le\rho$; precisely $\abs{F(z)}\le A'e^{B\abs z^\rho}$ with $B=(1+e^{-1})c'^{\rho}/\rho$ for any $c'>c$.

*Proof.* Fix $c'>c$; then $\abs{a_n}\le(c'n^{-1/\rho})^n$ for $n\ge N$. For $r\ge1$, $\abs z=r$ and $t=c'r$,
$$
\sum_{n\ge N}\abs{a_n}r^n\le\sum_{n\ge N}\bigl(t\,n^{-1/\rho}\bigr)^n .
$$
For every $n$, $\bigl(tn^{-1/\rho}\bigr)^n=\exp\bigl(n\log t-\frac n\rho\log n\bigr)\le e^{t^\rho/(e\rho)}$, the maximum of $u\mapsto u\log t-\frac u\rho\log u$ being attained at $u=t^\rho/e$. For $n\ge2t^\rho$, $n^{-1/\rho}\le2^{-1/\rho}t^{-1}$, so those terms are at most $2^{-n/\rho}$ and sum to at most $2$. Below $2t^\rho$ there are at most $2t^\rho$ indices, so
$$
\abs{F(z)}\le\sum_{n<N}\abs{a_n}r^n+2t^\rho e^{t^\rho/(e\rho)}+2\le e^{B'r^\rho}
$$
for $r\ge R$, $B'=(1+e^{-1})c'^\rho/\rho$; enlarging the constant to cover $\abs z\le R$ gives the claim. $\square$

*Step 5: the order is exactly $3/2$.* By (5), $\limsup_n\abs{a_n}^{1/n}n^{2/3}=e^{2/3}<\infty$, so Lemma 2 with $\rho=\frac32$ shows that $S=\operatorname{Ai}$ has order of growth $\le\frac32$. If it had order $\le\rho$ for some $\rho<\frac32$, Lemma 1 would give $\limsup_n\abs{a_n}^{1/n}n^{1/\rho}<\infty$; but by (5), along $n=3m$,
$$
\abs{a_n}^{1/n}n^{1/\rho}=e^{2/3}n^{1/\rho-2/3}\bigl(1+o(1)\bigr)\longrightarrow+\infty
\qquad\text{since } \tfrac1\rho-\tfrac23>0,
$$
a contradiction. Hence the order of growth of $\operatorname{Ai}$ is exactly $3/2$.

*Remark.* The numerical values of the first paragraph and the identity of part (a) were rechecked independently to $40$--$50$ digits (mpmath): $S(x)=\operatorname{Ai}(x)$ at $x=0.5,1,2,3$; $S(-x)=\operatorname{Ai}(-x)$ at $x=0.5,1,2,3,5,12$; the relation $(n+2)(n+3)a_{n+3}=a_n$ for $n\le40$; and the asymptotic (5) for $m\le2\cdot10^4$. These checks are not part of the proof.
:::
