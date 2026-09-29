---
schema: qual/card@1
id: P-BKS10-7B
kind: problem
title: Residues of $\cot z/z^2$ and the Basel sum $\sum_{n\ge1}1/n^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently computed the residues at zero and the nonzero integer multiples of pi, proved a uniform cotangent bound on half-integer square contours, and derived the limiting residue sum.
---

::: {.problem}
Find all residues of
$$
\frac{\cot z}{z^2}
$$
and use them to evaluate
$$
\frac1{1^2}+\frac1{2^2}+\frac1{3^2}+\cdots.
$$
:::

::: {.solution}
Set
$$
F(z)\coloneqq\frac{\cot z}{z^2}.
$$

::: pf

::: {.pf-step #residue-nonzero-n}
For every nonzero integer $n$,
$$
\operatorname{Res}_{z=n\pi}F(z)
=
\frac{1}{n^2\pi^2}.
$$

::: pf-proof
At $z=n\pi$, the function $\sin z$ has a simple zero and
$$
(\sin z)'\big|_{z=n\pi}
=
\cos(n\pi)
\neq
0.
$$
Therefore $\cot z=\cos z/\sin z$ has a simple pole there with residue
$$
\frac{\cos(n\pi)}{\cos(n\pi)}=1.
$$
Since $z^{-2}$ is holomorphic at $n\pi\neq0$, multiplication gives the
stated residue.
:::

:::

::: {.pf-step #residue-origin}
At the origin,
$$
\operatorname{Res}_{z=0}F(z)
=
-\frac13.
$$

::: pf-proof
The Taylor expansions at $0$ give
$$
\sin z
=
z-\frac{z^3}{6}+O(z^5),
\qquad
\cos z
=
1-\frac{z^2}{2}+O(z^4).
$$
Hence
$$
\begin{aligned}
\cot z
&=
\frac{1-z^2/2+O(z^4)}
{z(1-z^2/6+O(z^4))}\\
&=
\frac1z
\left(
1-\frac{z^2}{3}+O(z^4)
\right)\\
&=
\frac1z-\frac z3+O(z^3).
\end{aligned}
$$
Therefore
$$
F(z)
=
\frac1{z^3}
-\frac1{3z}
+O(z),
$$
whose residue is $-1/3$.
:::

:::

::: {.pf-step #cotangent-bound}
Let
$$
R_N\coloneqq\left(N+\frac12\right)\pi
$$
and let $\Gamma_N$ be the positively oriented square with vertices
$$
\pm R_N\pm iR_N.
$$
There is a constant $C$ independent of $N$ such that
$$
\abs{\cot z}\leq C
$$
for every $z\in\Gamma_N$.

::: pf-proof
On a vertical side,
$$
z=\left(N+\frac12\right)\pi+iy
$$
or its negative counterpart. Periodicity and the identity
$$
\cot\left(\frac\pi2+iy\right)
=
-i\tanh y
$$
give
$$
\abs{\cot z}\leq1.
$$

For $z=x+iy$,
$$
\abs{\sin z}^2
=
\sin^2x+\sinh^2y
$$
and
$$
\abs{\cos z}^2
=
\cos^2x+\sinh^2y.
$$
Thus on either horizontal side, where $\abs{y}=R_N\geq\pi/2$,
$$
\abs{\cot z}^2
\leq
\frac{1+\sinh^2R_N}{\sinh^2R_N}
=
\coth^2R_N
\leq
\coth^2(\pi/2).
$$
Hence one may take
$$
C\coloneqq\coth(\pi/2).
$$
:::

:::

::: {.pf-step #contour-vanishes}
The contour integrals satisfy
$$
\lim_{N\to\infty}
\int_{\Gamma_N}F(z)\,dz
=
0.
$$

::: pf-proof
Every point of $\Gamma_N$ satisfies
$$
\abs{z}\geq R_N,
$$
and the perimeter of $\Gamma_N$ is $8R_N$. By step [](#cotangent-bound){.pf-ref},
$$
\abs{F(z)}
\leq
\frac{C}{R_N^2}
$$
on the contour. Therefore
$$
\abs{
\int_{\Gamma_N}F(z)\,dz
}
\leq
8R_N\frac{C}{R_N^2}
=
\frac{8C}{R_N}
\longrightarrow0.
$$
:::

:::

::: {.pf-step #partial-sum-identity}
For every $N\geq1$,
$$
\frac{1}{2\pi i}
\int_{\Gamma_N}F(z)\,dz
=
-\frac13
+
\frac{2}{\pi^2}
\sum_{n=1}^N\frac1{n^2}.
$$

::: pf-proof
The poles inside $\Gamma_N$ are exactly
$$
n\pi,
\qquad
-N\leq n\leq N.
$$
The residue theorem, together with steps [](#residue-nonzero-n){.pf-ref} and [](#residue-origin){.pf-ref}, gives
$$
\begin{aligned}
\frac{1}{2\pi i}
\int_{\Gamma_N}F(z)\,dz
&=
-\frac13
+
\sum_{n=1}^N
\left(
\frac{1}{n^2\pi^2}
+
\frac{1}{n^2\pi^2}
\right)\\
&=
-\frac13
+
\frac{2}{\pi^2}
\sum_{n=1}^N\frac1{n^2}.
\end{aligned}
$$
:::

:::

::: {.pf-step #basel-sum}
The Basel sum is
$$
\boxed{
\sum_{n=1}^{\infty}\frac1{n^2}
=
\frac{\pi^2}{6}
}.
$$

::: pf-proof
Let $N\to\infty$ in step [](#partial-sum-identity){.pf-ref}. By step [](#contour-vanishes){.pf-ref}, the left-hand side tends
to $0$. Hence
$$
0
=
-\frac13
+
\frac{2}{\pi^2}
\sum_{n=1}^{\infty}\frac1{n^2},
$$
which rearranges to the displayed value.
:::

:::

::: pf-qed
Steps [](#residue-nonzero-n){.pf-ref} and [](#residue-origin){.pf-ref} give all residues of $F$, and step [](#basel-sum){.pf-ref} gives the
requested series evaluation.
:::

:::

:::
