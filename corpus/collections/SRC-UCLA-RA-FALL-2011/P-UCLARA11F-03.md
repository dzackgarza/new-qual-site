---
schema: qual/card@1
id: P-UCLARA11F-03
kind: problem
title: Continuity and decay of an Lp convolution
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $1<p,q<\infty$ with $1/p+1/q=1$.
Let $f\in L^p(\RR^3)$ and $g\in L^q(\RR^3)$.
Show that:

(a) $f*g$ is continuous on $\RR^3$;

(b) $(f*g)(x)\to0$ as $\norm{x}\to\infty$.
:::

::: {.solution}

For
$$
x\in\RR^3,
$$
define
$$
(f*g)(x)
=
\int_{\RR^3}
f(y)g(x-y)\,dy.
$$

By Hölder's inequality,
$$
\boxed{
\abs{(f*g)(x)}
\le
\norm{f}_{L^p}\norm{g}_{L^q}}
$$
for every $x$.

::: {.proof}
For fixed $x$, the function
$$
y\mapsto g(x-y)
$$
has the same $L^q$-norm as $g$. Thus
$$
\int \abs{f(y)g(x-y)}\,dy
\le
\norm{f}_p\norm{g(x-\cdot)}_q
=
\norm{f}_p\norm{g}_q.
$$
:::

## Translation continuity in $L^q$

For $h\in\RR^3$, write
$$
(\tau_h u)(z)=u(z+h).
$$

::: pf

::: {.pf-step #s1-1}

If $\varphi\in C_c(\RR^3)$, then
$$
\boxed{
\norm{\tau_h\varphi-\varphi}_{L^q}\to0
\qquad(h\to0)}.
$$


::: pf-proof

Let $K$ contain the support of $\varphi$, and choose a bounded neighborhood $K'$ containing
$$
K\cup(K-h)
$$
for all sufficiently small $h$.

Because $\varphi$ is uniformly continuous,
$$
\norm{\tau_h\varphi-\varphi}_\infty\to0.
$$
Therefore
$$
\norm{\tau_h\varphi-\varphi}_q^q
\le
\setmeasure{K'}\,
\norm{\tau_h\varphi-\varphi}_\infty^q
\to0.
$$

:::

:::

::: {.pf-step #s1-2}

For every $u\in L^q(\RR^3)$,
$$
\boxed{
\norm{\tau_hu-u}_{L^q}\to0
\qquad(h\to0)}.
$$


::: pf-proof

Fix $\varepsilon>0$. Choose
$$
\varphi\in C_c(\RR^3)
$$
with
$$
\norm{u-\varphi}_q<\varepsilon
$$
using density of $C_c$ in $L^q$.

Translations preserve the $L^q$-norm, so
$$
\begin{aligned}
\norm{\tau_hu-u}_q
&\le
\norm{\tau_h(u-\varphi)}_q
+
\norm{\tau_h\varphi-\varphi}_q
+
\norm{\varphi-u}_q\\
&<
2\varepsilon
+
\norm{\tau_h\varphi-\varphi}_q.
\end{aligned}
$$
By step [](#s1-1){.pf-ref}, the final term is $<\varepsilon$ for sufficiently small $h$. Since $\varepsilon$ is arbitrary, the result follows.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
(f*g)(x)
=
\int_{\RR^3}
f(y)\,
(\tau_x\widetilde g)(y)\,dy}.
$$


::: pf-proof

Since
$$
(\tau_x\widetilde g)(y)
=
\widetilde g(y+x)
=
g(-y-x)
$$
under this convention, instead use the equivalent translation
$$
(T_x\widetilde g)(y)=\widetilde g(y-x)=g(x-y).
$$
Thus, with
$$
T_xu(y)=u(y-x),
$$
$$
(f*g)(x)=\int f(y)(T_x\widetilde g)(y)\,dy.
$$
The $T_x$-translations satisfy the same norm-continuity as $\tau_h$.

:::

:::

::: {.pf-step #s1-4}

For $x,h\in\RR^3$,
$$
\abs{(f*g)(x+h)-(f*g)(x)}
\le
\norm{f}_p
\,
\norm{T_{x+h}\widetilde g-T_x\widetilde g}_q.
$$


::: pf-proof

Subtract the two integral expressions from step [](#s1-3){.pf-ref} and apply Hölder's inequality.

:::

:::

::: {.pf-step #s1-5}

The norm on the right satisfies
$$
\boxed{
\norm{T_{x+h}\widetilde g-T_x\widetilde g}_q
=
\norm{T_h\widetilde g-\widetilde g}_q}.
$$


::: pf-proof

Translation invariance of Lebesgue measure gives
$$
\norm{T_xv}_q=\norm{v}_q.
$$
Also
$$
T_{x+h}=T_xT_h.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
(f*g)(x+h)\to(f*g)(x)}
$$
as $h\to0$.


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref},
$$
\abs{(f*g)(x+h)-(f*g)(x)}
\le
\norm{f}_p
\,
\norm{T_h\widetilde g-\widetilde g}_q.
$$
The final norm tends to $0$ by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
f*g\in C(\RR^3)}.
$$


::: pf-proof

The point $x$ was arbitrary in step [](#s1-6){.pf-ref}.

:::

:::

::: pf-step

Let
$$
\varepsilon>0.
$$
Choose compactly supported functions
$$
f_0\in L^p(\RR^3),
\qquad
g_0\in L^q(\RR^3)
$$
such that
$$
\boxed{
\norm{f-f_0}_p
<
\frac{\varepsilon}{2(\norm{g}_q+1)}}
$$
and
$$
\boxed{
\norm{g-g_0}_q
<
\frac{\varepsilon}{2(\norm{f_0}_p+1)}}.
$$


::: pf-proof

Compactly supported functions are dense in $L^p$ and $L^q$. After choosing $f_0$, choose $g_0$ with the stated bounds.

:::

:::

::: pf-step

For every $x$,
$$
(f*g)(x)-(f_0*g_0)(x)
=
((f-f_0)*g)(x)
+
(f_0*(g-g_0))(x).
$$


::: pf-proof

Add and subtract $f_0*g$:
$$
f*g-f_0*g_0
=
(f-f_0)*g
+
f_0*(g-g_0).
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
\norm{f*g-f_0*g_0}_\infty
<
\varepsilon}.
$$


::: pf-proof

Using the Hölder convolution bound at the start,
$$
\begin{aligned}
\norm{f*g-f_0*g_0}_\infty
&\le
\norm{f-f_0}_p\norm{g}_q
+
\norm{f_0}_p\norm{g-g_0}_q\\
&<
\frac{\varepsilon}{2}
+
\frac{\varepsilon}{2}
=
\varepsilon.
\end{aligned}
$$
The harmless $+1$ terms in the denominators ensure the strict inequalities even when one norm vanishes.

:::

:::

::: {.pf-step #s1-11}

Since $f_0$ and $g_0$ have compact support,
$$
\boxed{
f_0*g_0
\text{ has compact support}.}
$$


::: pf-proof

If
$$
\operatorname{supp}f_0\subseteq K,
\qquad
\operatorname{supp}g_0\subseteq L,
$$
then
$$
\operatorname{supp}(f_0*g_0)
\subseteq
K+L
=
\{k+\ell:k\in K,\ \ell\in L\},
$$
which is compact.

:::

:::

::: {.pf-step #s1-12}

Hence there exists $R>0$ such that
$$
\boxed{
(f_0*g_0)(x)=0
\qquad\text{whenever }\norm{x}>R}.
$$


::: pf-proof

A compact subset of $\RR^3$ is bounded. Choose $R$ containing the compact support from step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

For $\norm{x}>R$,
$$
\boxed{
\abs{(f*g)(x)}<\varepsilon}.
$$


::: pf-proof

By step [](#s1-12){.pf-ref},
$$
(f_0*g_0)(x)=0.
$$
Hence
$$
\abs{(f*g)(x)}
=
\abs{(f*g)(x)-(f_0*g_0)(x)}
\le
\norm{f*g-f_0*g_0}_\infty
<
\varepsilon
$$
by step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
\boxed{
(f*g)(x)\to0
\qquad(\norm{x}\to\infty)}.
$$


::: pf-proof

Step [](#s1-13){.pf-ref} is the definition of vanishing at infinity.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves part (a), and step [](#s1-14){.pf-ref} proves part (b).

:::

:::

:::
