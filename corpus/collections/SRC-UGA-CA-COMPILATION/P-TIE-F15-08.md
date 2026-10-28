---
schema: qual/card@1
id: P-TIE-F15-08
kind: problem
title: Taylor coefficient ratios detect a pole on the unit circle
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 8.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the source wording of Fall 2015, question 8, page 10 of Questions_from_Tie.pdf, and moved the note on the expression the source omits for c_n into a remark.
---

::: {.problem}
Suppose that $f$ is holomorphic in an open set containing the closed unit disc, except for a pole at $z_0$ on the unit circle. Let denote the the power series in the open disc. Show that (1) $c_n \ne 0$ for all large enough $n$'s, and (2) $\lim_{n\to\infty} \frac{c_n}{c_{n+1}} = z_0$.
:::

::: {.remark}
The source omits the defining expression between "Let" and "denote", so the coefficients $c_n$ are never introduced.
From the conclusions, the missing text defines $c_n$ as the coefficients of the power series expansion of $f$ in the open unit disc, $f(z) = \sum_{n=0}^\infty c_n z^n$ for $\abs{z} < 1$; the source does not supply this wording.
:::

::: {.solution}

Use the intended coefficients described in the remark:
$$
f(z)=\sum_{n=0}^{\infty}c_nz^n,
\qquad
\abs{z}<1.
$$
Let the pole of $f$ at $z_0$ have order $m\ge1$.

::: pf

::: {.pf-step #s1-1}

There exist coefficients $a_{-1},\ldots,a_{-m}$ with $a_{-m}\ne0$ and a function $h$ holomorphic on a disk $\abs{z}<\rho$ for some $\rho>1$ such that
$$
f(z)
=
h(z)
+
\sum_{j=1}^{m}
\frac{a_{-j}}{(z-z_0)^j}.
$$


::: pf-proof

Because $f$ is holomorphic in an open neighborhood of the closed unit disk except for the pole at $z_0$, compactness gives a number $\rho>1$ such that $f$ is meromorphic on $\abs{z}<\rho$ with no singularity there except $z_0$. The Laurent expansion of $f$ at the pole has a finite principal part
$$
\sum_{j=1}^{m}\frac{a_{-j}}{(z-z_0)^j},
\qquad
a_{-m}\ne0.
$$
Subtracting this principal part removes the pole, so the difference extends holomorphically across $z_0$. Denote the resulting holomorphic function by $h$.

:::

:::

::: {.pf-step #s1-2}

For every $j\ge1$ and $\abs{z}<1$,
$$
\frac1{(z-z_0)^j}
=
(-1)^j
\sum_{n=0}^{\infty}
\binom{n+j-1}{j-1}
z_0^{-n-j}z^n.
$$


::: pf-proof

Since $\abs{z}<1=\abs{z_0}$,
$$
\abs{\frac{z}{z_0}}<1.
$$
Thus
$$
\begin{aligned}
\frac1{(z-z_0)^j}
&=
\frac{(-1)^j}{z_0^j}
\left(1-\frac{z}{z_0}\right)^{-j}\\
&=
\frac{(-1)^j}{z_0^j}
\sum_{n=0}^{\infty}
\binom{n+j-1}{j-1}
\left(\frac{z}{z_0}\right)^n,
\end{aligned}
$$
which is the claimed expansion.

:::

:::

::: {.pf-step #s1-3}

There is a polynomial $P(n)$ of degree $m-1$ with nonzero leading coefficient such that
$$
c_n
=
z_0^{-n}P(n)+h_n,
$$
where
$$
h(z)=\sum_{n=0}^{\infty}h_nz^n.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, comparison of Taylor coefficients gives
$$
c_n
=
h_n
+
\sum_{j=1}^{m}
a_{-j}(-1)^j
\binom{n+j-1}{j-1}
z_0^{-n-j}.
$$
Factor out $z_0^{-n}$ and define
$$
P(n)
\coloneqq
\sum_{j=1}^{m}
a_{-j}(-1)^jz_0^{-j}
\binom{n+j-1}{j-1}.
$$
For fixed $j$, the binomial coefficient is a polynomial in $n$ of degree $j-1$. Hence $P$ has degree at most $m-1$. Its degree-$m-1$ term comes only from $j=m$ and has coefficient
$$
\frac{a_{-m}(-1)^mz_0^{-m}}{(m-1)!},
$$
which is nonzero. Thus $\deg P=m-1$.

:::

:::

::: {.pf-step #s1-4}

For some $r>1$ and some constant $C>0$,
$$
\abs{h_n}\le Cr^{-n}
$$
for all $n$.


::: pf-proof

Choose $r$ with
$$
1<r<\rho.
$$
Since $h$ is holomorphic on $\abs{z}<\rho$, it is bounded on the circle $\abs{z}=r$; let
$$
M_r\coloneqq\max_{\abs{z}=r}\abs{h(z)}.
$$
Cauchy's coefficient estimate gives
$$
\abs{h_n}\le M_rr^{-n}.
$$
Take $C=M_r$.

:::

:::

::: {.pf-step #s1-5}

The coefficients $c_n$ are nonzero for all sufficiently large $n$.


::: pf-proof

Since $\abs{z_0}=1$, step [](#s1-3){.pf-ref} gives
$$
z_0^nc_n
=
P(n)+z_0^nh_n.
$$
By step [](#s1-4){.pf-ref},
$$
\abs{z_0^nh_n}
=
\abs{h_n}
\le
Cr^{-n}.
$$
If $m=1$, then $P$ is a nonzero constant. If $m>1$, then
$$
\abs{P(n)}
\sim
C_0n^{m-1}
$$
for some $C_0>0$. In either case,
$$
\frac{\abs{z_0^nh_n}}{\abs{P(n)}}\longrightarrow0.
$$
Hence for all sufficiently large $n$,
$$
\abs{z_0^nh_n}<\frac12\abs{P(n)}.
$$
Therefore
$$
\abs{z_0^nc_n}
\ge
\abs{P(n)}-\abs{z_0^nh_n}
>
\frac12\abs{P(n)}
>0,
$$
so $c_n\ne0$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
\lim_{n\to\infty}\frac{c_n}{c_{n+1}}=z_0.
}
$$


::: pf-proof

Set
$$
\varepsilon_n\coloneqq z_0^nh_n.
$$
Then step [](#s1-3){.pf-ref} becomes
$$
c_n
=
z_0^{-n}\left(P(n)+\varepsilon_n\right),
$$
and step [](#s1-4){.pf-ref} gives $\varepsilon_n=O(r^{-n})$. By step [](#s1-5){.pf-ref}, the denominator below is nonzero for large $n$, and
$$
\frac{c_n}{c_{n+1}}
=
z_0
\frac{P(n)+\varepsilon_n}
{P(n+1)+\varepsilon_{n+1}}.
$$
Because $P$ is a nonzero polynomial,
$$
\frac{P(n)}{P(n+1)}\longrightarrow1,
$$
and the exponential decay of $\varepsilon_n$ implies
$$
\frac{\varepsilon_n}{P(n)}\longrightarrow0,
\qquad
\frac{\varepsilon_{n+1}}{P(n+1)}\longrightarrow0.
$$
Therefore
$$
\frac{P(n)+\varepsilon_n}
{P(n+1)+\varepsilon_{n+1}}
\longrightarrow1,
$$
which proves the claimed limit.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (1), and step [](#s1-6){.pf-ref} proves part (2).

:::

:::

:::
