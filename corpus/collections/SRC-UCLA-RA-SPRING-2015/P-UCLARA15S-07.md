---
schema: qual/card@1
id: P-UCLARA15S-07
kind: problem
title: Holomorphic maps from the disk to the upper half-plane with $f_n(0)\to0$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let
\[
D=\{z\in\mathbb C:|z|<1\},\qquad \mathbb C_+=\{z\in\mathbb C:\operatorname{Im}z>0\}.
\]
Suppose $f_n:D\to\mathbb C_+$ is a sequence of holomorphic functions and $f_n(0)\to0$ as $n\to\infty$.
Show that $f_n(z)\to0$ uniformly on compact subsets of $D$.
:::

::: {.solution}
Define the Cayley transform
\[
\Phi(w)
\coloneqq
\frac{w-i}{w+i},
\qquad
\Phi^{-1}(\zeta)
=
i\frac{1+\zeta}{1-\zeta},
\]
and set
\[
g_n
\coloneqq
\Phi\circ f_n:D\to D.
\]

<1>1. One has
\[
a_n
\coloneqq
g_n(0)
\longrightarrow
-1.
\]

::: {.proof}
Since $f_n(0)\to0$ and $\Phi$ is continuous at $0$,
\[
a_n
=
\Phi(f_n(0))
\longrightarrow
\Phi(0)
=-1.
\]
:::

<1>2. Define
\[
h_n(z)
\coloneqq
\frac{g_n(z)-a_n}
{1-\overline{a_n}g_n(z)}.
\]
Then $h_n:D\to D$ is holomorphic, $h_n(0)=0$, and
\[
|h_n(z)|\le|z|
\qquad
(z\in D).
\]

::: {.proof}
The map
\[
\zeta\longmapsto
\frac{\zeta-a_n}{1-\overline{a_n}\zeta}
\]
is an automorphism of $D$ sending $a_n$ to $0$. Therefore $h_n$ is a holomorphic self-map of $D$ with $h_n(0)=0$. Schwarz's lemma gives the stated inequality.
:::

<1>3. For every $0<r<1$,
\[
\sup_{|z|\le r}|g_n(z)-a_n|
\longrightarrow0.
\]

::: {.proof}
Solving the relation in step <1>2 for $g_n$ gives
\[
g_n(z)
=
\frac{a_n+h_n(z)}
{1+\overline{a_n}h_n(z)}.
\]
Hence
\[
g_n(z)-a_n
=
\frac{(1-|a_n|^2)h_n(z)}
{1+\overline{a_n}h_n(z)}.
\]
For $|z|\le r$, step <1>2 gives $|h_n(z)|\le r$, so
\[
|1+\overline{a_n}h_n(z)|
\ge
1-|a_n|r
\ge
1-r.
\]
Therefore
\[
\sup_{|z|\le r}
|g_n(z)-a_n|
\le
\frac{r(1-|a_n|^2)}{1-r}.
\]
By step <1>1, $|a_n|\to1$, so the right-hand side tends to $0$.
:::

<1>4. For every $0<r<1$,
\[
g_n\longrightarrow-1
\]
uniformly on $\{|z|\le r\}$.

::: {.proof}
By the triangle inequality,
\[
\sup_{|z|\le r}|g_n(z)+1|
\le
\sup_{|z|\le r}|g_n(z)-a_n|
+
|a_n+1|.
\]
The first term tends to $0$ by step <1>3, and the second tends to $0$ by step <1>1.
:::

<1>5. For every $0<r<1$,
\[
\boxed{
f_n\longrightarrow0
\text{ uniformly on }\{|z|\le r\}
}.
\]

::: {.proof}
Since
\[
f_n
=
\Phi^{-1}(g_n)
=
i\frac{1+g_n}{1-g_n},
\]
step <1>4 gives
\[
1+g_n\longrightarrow0
\]
uniformly on $|z|\le r$, while
\[
1-g_n\longrightarrow2
\]
uniformly there. Hence the quotient tends uniformly to $0$.
:::

<1>6. $f_n\to0$ uniformly on compact subsets of $D$.

::: {.proof}
Every compact subset of $D$ is contained in a closed disk
\[
\{|z|\le r\}
\]
for some $r<1$. Apply step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
