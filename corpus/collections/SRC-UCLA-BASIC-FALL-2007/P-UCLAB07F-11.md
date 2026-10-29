---
schema: qual/card@1
id: P-UCLAB07F-11
kind: problem
title: Riemann integrability of a bounded function versus its cube
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Let $f$ be a bounded real-valued function on $[0,1]$.
Show that $f$ is Riemann integrable if and only if $f^3$ is Riemann integrable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let $h:[0,1]\to\RR$ be bounded and Riemann integrable, and let $\phi$ be continuous on a closed interval containing the range of $h$. Then $\phi\circ h$ is Riemann integrable.


::: pf-proof

Choose $M>0$ such that
\[
|h(x)|\le M
\]
for all $x$, and let
\[
K=\max_{|t|\le M}|\phi(t)|.
\]
If $K=0$, then $\phi\circ h=0$ and there is nothing to prove. Assume $K>0$.

Fix $\varepsilon>0$. Uniform continuity of $\phi$ on $[-M,M]$ gives $\delta>0$ such that
\[
|s-t|<\delta
\quad\Longrightarrow\quad
|\phi(s)-\phi(t)|<\frac{\varepsilon}{2}.
\]
Since $h$ is Riemann integrable, there is a partition
\[
P:\quad 0=x_0<\cdots<x_m=1
\]
such that
\[
U(h,P)-L(h,P)
<
\frac{\varepsilon\delta}{4K}.
\]

For each subinterval
\[
I_i=[x_{i-1},x_i],
\]
let
\[
\omega_i
=
\sup_{I_i}h-\inf_{I_i}h.
\]
Call $I_i$ good if $\omega_i<\delta$ and bad otherwise.

On a good interval, the oscillation of $\phi\circ h$ is at most $\varepsilon/2$. On every interval, it is at most $2K$. Moreover, for the bad intervals,
\[
\delta\sum_{\mathrm{bad}}|I_i|
\le
\sum_{\mathrm{bad}}\omega_i|I_i|
\le
U(h,P)-L(h,P),
\]
so
\[
\sum_{\mathrm{bad}}|I_i|
<
\frac{\varepsilon}{4K}.
\]
Hence
\[
\begin{aligned}
U(\phi\circ h,P)-L(\phi\circ h,P)
&\le
\frac{\varepsilon}{2}\sum_{\mathrm{good}}|I_i|
+
2K\sum_{\mathrm{bad}}|I_i|\\
&<
\frac{\varepsilon}{2}
+
\frac{\varepsilon}{2}
=
\varepsilon.
\end{aligned}
\]
By the Darboux criterion, $\phi\circ h$ is Riemann integrable.

:::

:::

::: {.pf-step #s1-2}

If $f$ is Riemann integrable, then $f^3$ is Riemann integrable.


::: pf-proof

Apply step [](#s1-1){.pf-ref} with
\[
h=f
\]
and
\[
\phi(t)=t^3.
\]
The function $\phi$ is continuous on every bounded interval.

:::

:::

::: {.pf-step #s1-3}

If $f^3$ is Riemann integrable, then $f$ is Riemann integrable.


::: pf-proof

Since $f$ is bounded, so is $f^3$. Apply step [](#s1-1){.pf-ref} with
\[
h=f^3
\]
and
\[
\phi(t)=\sqrt[3]{t}.
\]
The real cube-root function is continuous on every bounded interval, and
\[
(\phi\circ h)(x)
=
\sqrt[3]{f(x)^3}
=
f(x).
\]
Thus $f$ is Riemann integrable.

:::

:::

::: {.pf-step #s1-4}

Therefore
\[
\boxed{
f\text{ is Riemann integrable}
\iff
f^3\text{ is Riemann integrable}
}.
\]


::: pf-proof

Step [](#s1-2){.pf-ref} proves the forward implication, and step [](#s1-3){.pf-ref} proves the reverse implication.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required equivalence.

:::

:::

:::
