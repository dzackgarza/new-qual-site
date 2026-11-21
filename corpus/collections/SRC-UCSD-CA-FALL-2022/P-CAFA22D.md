---
schema: qual/card@1
id: P-CAFA22D
kind: problem
title: Mean value inequality and completeness of $A^1(G)$
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Part (i): the circle mean value
    inequality for the subharmonic |f|, multiplied by 2 rho and integrated in rho, gives
    r^2 |f(a)| <= (1/pi) int_B |f| dA, which after dividing by the area pi r^2 is the stated bound.
    Part (ii): the prose's "closedness in L^1" is now derived — the estimate of (i) with
    f_n - f_m bounds |f_n(a) - f_m(a)| by (1/(pi r^2)) ||f_n - f_m||_1 uniformly on a compact K, so
    the sequence is uniformly Cauchy there, and Weierstrass gives a holomorphic limit; a
    subsequence converges pointwise a.e. to the L^1 limit, so the two agree a.e. and the limit lies
    in A^1(G). Completeness then follows from completeness of L^1. One point is stated rather than
    glossed: A^1(G) is being read as a set of L^1 classes, which is what the metric d(f,g) =
    ||f - g||_1 makes it. Statement unchanged; the card says the argument is its own.
---

::: {.problem}
Let $G \subset \CC$ be a bounded region.

(i) Show that if $f \in H(G)$ and $B = B(a,r) \subset G$, then
$$
\abs{f(a)} \leq \frac{1}{\setmeasure{B}} \int_B \abs{f(z)}\,dx\,dy,
$$
where $\setmeasure{B}$ denotes the area of $B$.

(ii) Show that the space
$$
A^1(G) = \{f \in H(G) : \norm{f}_1 := \int_G \abs{f(z)}\,dx\,dy < \infty\}
$$
endowed with the metric $d(f,g) = \norm{f - g}_1$ is complete.

Note: You may use the result in part (i) even if you did not prove this.
:::

::: {.solution}
Part (i) is the mean value inequality integrated over the disc: averaging the circle means over radius $\rho$ against $2\rho$ gives the area mean. Part (ii) then follows because (i) converts $L^1$-convergence into local uniform convergence, so a Cauchy sequence in $A^1(G)$ converges locally uniformly to a holomorphic function, which is the same $L^1$ function; hence $A^1(G)$ is a closed subspace of $L^1(G)$, which is complete. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #mean}
(i) For $f\in H(G)$, $a\in G$ and $0<\rho<r$ with $\overline{B(a,r)}\subset G$,
$$
\abs{f(a)}\le\frac1{2\pi}\int_0^{2\pi}\abs{f(a+\rho e^{it})}\dt .
$$

::: pf-proof
$f$ is holomorphic near the closed disc, so $\abs f$ is subharmonic there and satisfies the mean value inequality: $\abs{f(a)}$ is at most the average of $\abs f$ over the circle of radius $\rho$ about $a$, for every $\rho$ small enough that the closed disc lies in $G$. Since $B(a,r)\subset G$ and $\rho<r$, the circle of radius $\rho$ lies in $G$.
:::

:::


::: {.pf-step #area}
(i) $r^2\abs{f(a)}\le\dfrac1\pi\displaystyle\int_{B(a,r)}\abs{f(z)}\dA(z)$, hence $\abs{f(a)}\le\dfrac{1}{\abs B}\displaystyle\int_B\abs{f}$ with $\abs B=\pi r^2$.

::: pf-proof
Multiply the inequality of step [](#mean){.pf-ref} by $2\rho>0$ and integrate over $\rho\in(0,r)$: the left side becomes $\abs{f(a)}\int_0^r2\rho\,d\rho=r^2\abs{f(a)}$, and the right side becomes $\frac1\pi\int_0^r\!\!\int_0^{2\pi}\abs{f(a+\rho e^{it})}\rho\dt\,d\rho$, which is $\frac1\pi\int_{B(a,r)}\abs f\dA$ by the polar-coordinate formula for the area integral (the integrand is continuous and the disc is compact inside $G$). Dividing by $\pi r^2=\abs B$ gives the second display.
:::

:::


::: {.pf-step #local-uniform}
(ii) If $f_n\to f$ in $L^1(G)$ with $f_n\in H(G)$, then $f_n$ converges uniformly on every compact $K\subset G$.

::: pf-proof
Let $K\subset G$ be compact and choose $r>0$ with $\overline{B(a,r)}\subset G$ for every $a\in K$ — possible since $K$ is compact and $G$ is open, e.g. $2r<\operatorname{dist}(K,\partial G)$ if $G\ne\CC$, and if $G=\CC$ any fixed $r$ works after shrinking. For $a\in K$, step [](#area){.pf-ref} applied to $f_n-f_m$ gives
$$
\abs{f_n(a)-f_m(a)}\le\frac{1}{\pi r^2}\int_{B(a,r)}\abs{f_n-f_m}\le\frac{1}{\pi r^2}\norm{f_n-f_m}_{L^1(G)},
$$
so the sequence is uniformly Cauchy on $K$. Note $K$ is covered by finitely many discs $B(a,r)$ with $a\in K$ by compactness, so a single $r$ works for all of $K$ after shrinking once, and the bound is uniform in $a\in K$.
:::

:::


::: {.pf-step #limit}
(ii) The limit $f$ agrees almost everywhere with a holomorphic function.

::: pf-proof
By step [](#local-uniform){.pf-ref} the sequence converges uniformly on compact subsets of $G$ to a function $g$; by Weierstrass's theorem a locally uniform limit of holomorphic functions is holomorphic, so $g\in H(G)$. On the other hand $f_n\to f$ in $L^1(G)$, hence in $L^1_{\mathrm{loc}}$, hence a subsequence converges to $f$ pointwise almost everywhere; that subsequence also converges to $g$ pointwise everywhere, so $f=g$ almost everywhere. In particular $\norm f_1=\norm g_1<\infty$ and $g\in A^1(G)$.
:::

:::


::: {.pf-step #closed}
(ii) $A^1(G)$ is a closed subset of $L^1(G)$.

::: pf-proof
Let $(f_n)\subset A^1(G)$ converge to $f\in L^1(G)$. By steps [](#local-uniform){.pf-ref} and [](#limit){.pf-ref} there is $g\in A^1(G)$ with $f=g$ almost everywhere, and two functions equal almost everywhere have the same $L^1$ class; so the limit class lies in $A^1(G)$ once $A^1(G)$ is read as a set of classes, which is the identification the metric $d(f,g)=\norm{f-g}_1$ makes. Hence $A^1(G)$ is closed in $L^1(G)$.
:::

:::


::: {.pf-step #complete}
(ii) $(A^1(G),d)$ is complete.

::: pf-proof
Let $(f_n)$ be Cauchy for $d$. Since $d$ is the $L^1$ metric, $(f_n)$ is Cauchy in $L^1(G)$, which is complete, so it converges in $L^1$ to some $f\in L^1(G)$; by step [](#closed){.pf-ref} the limit lies in $A^1(G)$. So every Cauchy sequence converges, which is completeness.
:::

:::


::: {.pf-step #conclusion}
Both (i) and (ii) hold.

::: pf-proof
Step [](#area){.pf-ref} is (i) and step [](#complete){.pf-ref} is (ii); the only inputs are the subharmonic mean value inequality, polar coordinates, Weierstrass's theorem and the completeness of $L^1$.
:::

:::

:::
:::
