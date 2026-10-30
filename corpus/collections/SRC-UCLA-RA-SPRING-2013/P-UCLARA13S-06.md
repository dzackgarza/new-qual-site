---
schema: qual/card@1
id: P-UCLARA13S-06
kind: problem
title: Fourier transforms form a dense proper subspace of C0
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Define
$$
X=\left\{\xi\longmapsto\int_{\RR}e^{i\xi x}f(x)\,dx:\ f\in L^1(\RR)\right\}.
$$
Show that

(a) $X\subset C_0(\RR)$;

(b) $X$ is dense in $C_0(\RR)$;

(c) $X\ne C_0(\RR)$.
:::

::: {.solution}

For $f\in L^1(\RR)$, write
$$
\mathcal Ff(\xi)
\coloneqq
\int_{\RR}e^{i\xi x}f(x)\,dx.
$$

::: pf

::: {.pf-step #s1-1}

For every $f\in L^1(\RR)$, the function $\mathcal Ff$ is continuous.


::: pf-proof

Fix $\xi_0\in\RR$. If $\xi\to\xi_0$, then for every $x$,
$$
e^{i\xi x}f(x)
\longrightarrow
e^{i\xi_0x}f(x),
$$
while
$$
\abs{e^{i\xi x}f(x)}
=
\abs{f(x)}.
$$
Since $\abs{f}\in L^1$, dominated convergence gives
$$
\mathcal Ff(\xi)
\longrightarrow
\mathcal Ff(\xi_0).
$$

:::

:::

::: {.pf-step #s1-2}

For every $f\in L^1(\RR)$,
$$
\mathcal Ff(\xi)\longrightarrow0
\qquad
(\abs{\xi}\to\infty).
$$


::: pf-proof

Fix $\varepsilon>0$. Choose
$$
\phi\in C_c^1(\RR)
$$
such that
$$
\norm{f-\phi}_1<\frac{\varepsilon}{2};
$$
the space $C_c^1(\RR)$ is dense in $L^1(\RR)$.

For $\xi\ne0$, integration by parts gives
$$
\mathcal F\phi(\xi)
=
-\frac1{i\xi}
\int_{\RR}
e^{i\xi x}\phi'(x)\,dx,
$$
because $\phi$ has compact support. Hence
$$
\abs{\mathcal F\phi(\xi)}
\le
\frac{\norm{\phi'}_1}{\abs{\xi}}
\longrightarrow0.
$$
Also,
$$
\abs{\mathcal F(f-\phi)(\xi)}
\le
\norm{f-\phi}_1
<
\frac\varepsilon2.
$$
For sufficiently large $\abs{\xi}$, the first term is also less than $\varepsilon/2$, so
$$
\abs{\mathcal Ff(\xi)}<\varepsilon.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{X\subset C_0(\RR)}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that every element of $X$ is continuous and vanishes at infinity.

:::

:::

::: {.pf-step #s1-4}

Every Schwartz function belongs to $X$.


::: pf-proof

The Fourier transform is a bijection
$$
\mathcal S(\RR)
\longrightarrow
\mathcal S(\RR)
$$
for any fixed standard Fourier normalization. Thus if
$$
h\in\mathcal S(\RR),
$$
there is $g\in\mathcal S(\RR)\subset L^1(\RR)$ such that
$$
h=\mathcal Fg
$$
with the sign convention used here after replacing the variable by its negative if necessary. Hence $h\in X$.

:::

:::

::: {.pf-step #s1-5}

The Schwartz space is dense in $C_0(\RR)$ in the supremum norm.


::: pf-proof

Fix $h\in C_0(\RR)$ and $\varepsilon>0$. Choose $R>0$ so that
$$
\abs{h(x)}<\varepsilon
\qquad
(\abs{x}>R).
$$
Choose a smooth cutoff $\chi\in C_c^\infty(\RR)$ with
$$
0\le\chi\le1,
\qquad
\chi=1\text{ on }[-R,R].
$$
Then
$$
\norm{h-\chi h}_\infty<\varepsilon.
$$

The continuous compactly supported function $\chi h$ is uniformly continuous. Let $(\rho_\delta)$ be a standard smooth approximate identity. For sufficiently small $\delta>0$,
$$
\norm{\rho_\delta*(\chi h)-\chi h}_\infty<\varepsilon.
$$
The convolution
$$
\rho_\delta*(\chi h)
$$
is smooth and compactly supported, hence is a Schwartz function. Thus every $h\in C_0$ is uniformly approximated by Schwartz functions.

:::

:::

::: {.pf-step #s1-6}

The subspace $X$ is dense in $C_0(\RR)$.


::: pf-proof

By step [](#s1-4){.pf-ref}, $X$ contains the Schwartz space. By step [](#s1-5){.pf-ref}, the latter is dense in $C_0(\RR)$.

:::

:::

::: {.pf-step #s1-7}

The Fourier transform
$$
\mathcal F:L^1(\RR)\to C_0(\RR)
$$
is bounded and injective.


::: pf-proof

For every $f\in L^1$,
$$
\norm{\mathcal Ff}_\infty
\le
\norm{f}_1,
$$
so $\mathcal F$ is bounded. Injectivity is the standard uniqueness theorem for the Fourier transform on $L^1(\RR)$.

:::

:::

::: {.pf-step #s1-8}

Suppose, toward a contradiction, that
$$
X=C_0(\RR).
$$
Then there is a constant $C>0$ such that
$$
\norm{f}_1
\le
C\norm{\mathcal Ff}_\infty
\qquad
(f\in L^1(\RR)).
$$


::: pf-proof

Under the assumption, step [](#s1-7){.pf-ref} makes
$$
\mathcal F:L^1(\RR)\to C_0(\RR)
$$
a bounded linear bijection between Banach spaces. By the open mapping theorem, its inverse is bounded. The displayed estimate is exactly boundedness of that inverse.

:::

:::

::: {.pf-step #s1-9}

There exists a sequence $(h_j)\subset C_c^\infty(\RR)$ such that
$$
\sup_j\norm{h_j}_\infty<\infty
$$
and
$$
h_j\longrightarrow
h
\coloneqq
\mathbf 1_{[-1,1]}
$$
in $L^2(\RR)$.


::: pf-proof

Take a standard smooth approximation of the indicator with values in $[0,1]$, for example by convolving $\mathbf 1_{[-1,1]}$ with compactly supported mollifiers and, if necessary, multiplying by a fixed compactly supported cutoff equal to $1$ near $[-1,1]$. Then
$$
0\le h_j\le1
$$
and $h_j\to h$ pointwise almost everywhere with supports contained in one fixed compact interval. Dominated convergence gives convergence in $L^2$, and the supremum norms are bounded by $1$.

:::

:::

::: {.pf-step #s1-10}

Let
$$
g_j=\mathcal F^{-1}h_j.
$$
Then each $g_j$ is Schwartz, hence in $L^1\cap L^2$, and there is $g\in L^2$ such that
$$
g_j\longrightarrow g
$$
in $L^2$ and, after passing to a subsequence,
$$
g_j(x)\longrightarrow g(x)
$$
for almost every $x$.


::: pf-proof

Because $h_j\in C_c^\infty\subset\mathcal S$, Fourier inversion gives $g_j\in\mathcal S$.

By the Plancherel theorem, the Fourier transform extends to an isomorphism of $L^2$ with itself, up to the fixed normalization constant. Since $h_j\to h$ in $L^2$, their inverse transforms converge in $L^2$ to the inverse Plancherel transform $g$ of $h$. Every $L^2$-convergent sequence has a subsequence converging pointwise almost everywhere.

:::

:::

::: {.pf-step #s1-11}

The function $g$ from step [](#s1-10){.pf-ref} does not belong to $L^1(\RR)$.


::: pf-proof

Suppose instead that $g\in L^1$. Then by step [](#s1-3){.pf-ref}, its $L^1$ Fourier transform has a continuous representative in $C_0(\RR)$. By compatibility of the $L^1$ and $L^2$ Fourier transforms, that continuous representative agrees almost everywhere with
$$
h=\mathbf 1_{[-1,1]}.
$$

No continuous function can agree almost everywhere with this indicator. Indeed, equality almost everywhere forces the continuous function to equal $1$ throughout $(-1,1)$, because the set on which it equals $1$ is dense there; similarly it must equal $0$ throughout $(1,\infty)$. Continuity at $1$ is then impossible. Hence $g\notin L^1$.

:::

:::

::: {.pf-step #s1-12}

One has
$$
\liminf_{j\to\infty}\norm{g_j}_1
=
\infty.
$$


::: pf-proof

Along the almost-everywhere convergent subsequence from step [](#s1-10){.pf-ref}, Fatou's lemma gives
$$
\int_{\RR}\abs{g(x)}\,dx
\le
\liminf_{j\to\infty}
\int_{\RR}\abs{g_j(x)}\,dx.
$$
The left-hand side is infinite by step [](#s1-11){.pf-ref}, so the liminf is infinite.

:::

:::

::: {.pf-step #s1-13}

The surjectivity assumption in step [](#s1-8){.pf-ref} is impossible.


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
\norm{g_j}_1
\le
C\norm{\mathcal Fg_j}_\infty
=
C\norm{h_j}_\infty.
$$
The right-hand side is uniformly bounded by step [](#s1-9){.pf-ref}, contradicting step [](#s1-12){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
\boxed{X\ne C_0(\RR)}.
$$


::: pf-proof

Step [](#s1-13){.pf-ref} contradicts the only alternative $X=C_0$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), step [](#s1-6){.pf-ref} proves part (b), and step [](#s1-14){.pf-ref} proves part (c).

:::

:::

:::
