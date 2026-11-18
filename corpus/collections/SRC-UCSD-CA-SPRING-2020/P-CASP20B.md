---
schema: qual/card@1
id: P-CASP20B
kind: problem
title: 'A holomorphic function on $\abs z>3$ with a prescribed derivative'
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residue Theorem
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Prove or disprove the following statement.

Let $U = \{z \in \CC : \abs{z} > 3\}$.
There exists a holomorphic function $f$ in $U$ such that
$$
f'(z) = \frac{z^2 + 2}{z(z-1)(z-2)}.
$$
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/Complex-Analysis-Qual-SP20.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. The earlier version of the card computed the integral through the residue at infinity, a convention it did not state; the computation below uses the residues at the three poles inside the circle, and the two agree.

Throughout, $U\coloneqq\theset{z\in\CC\mid\abs{z}>3}$ and
$$
R(z)\coloneqq\frac{z^{2}+2}{z(z-1)(z-2)}.
$$

::: pf

::: {.pf-step #holomorphic}
$R$ is holomorphic on $U$, and for every $r>3$ the circle $\abs{z}=r$ lies in $U$.

::: pf-proof
The denominator $z(z-1)(z-2)$ vanishes exactly at $0,1,2$, none of which lies in $U$ since $\abs{0},\abs{1},\abs{2}\leq2<3$, so $R$ is a quotient of holomorphic functions with nonvanishing denominator on $U$. If $r>3$ then every point of the circle satisfies $\abs{z}=r>3$, so the circle is contained in $U$.
:::

:::

::: {.pf-step #integral}
For every $r>3$,
$$
\int_{\abs{z}=r}R(z)\,dz=2\pi i\neq0,
$$
the circle being traversed counterclockwise.

:::: pf-proof

::: {.pf-step #residues}
The residues of $R$ at $0$, $1$ and $2$ are $1$, $-3$ and $3$.

::: pf-proof
All three poles are simple, so the residue at a pole $c$ is $\lim_{z\to c}(z-c)R(z)$. At $0$: $\lim_{z\to0}\frac{z^{2}+2}{(z-1)(z-2)}=\frac{2}{(-1)(-2)}=1$. At $1$: $\lim_{z\to1}\frac{z^{2}+2}{z(z-2)}=\frac{3}{1\cdot(-1)}=-3$. At $2$: $\lim_{z\to2}\frac{z^{2}+2}{z(z-1)}=\frac{6}{2\cdot1}=3$.
:::

:::

::: {.pf-step #residue-theorem}
$\int_{\abs{z}=r}R\,dz=2\pi i\,(1-3+3)=2\pi i$.

::: pf-proof
For $r>3$ the circle encloses the three simple poles and no others, and $R$ is holomorphic on and inside the circle apart from them, so the residue theorem gives the integral as $2\pi i$ times the sum of the three residues computed in step [](#residues){.pf-ref}.
:::

:::

::::

:::

::: pf-step
Therefore no holomorphic $f$ on $U$ satisfies $f'=R$ there, so the statement is false.

::: pf-proof
Suppose $f$ holomorphic on $U$ with $f'=R$. Fix $\gamma(t)\coloneqq r\mathrm{e}^{2\pi it}$ for $t\in[0,1]$, a closed piecewise smooth curve in $U$ by step [](#holomorphic){.pf-ref} with $r>3$. Then
$$
\int_{\gamma}R(z)\,dz=\int_{\gamma}f'(z)\,dz=f(\gamma(1))-f(\gamma(0))=0
$$
by the fundamental theorem of calculus for line integrals, since $f'$ is continuous and $f$ is a primitive of $R$ along the curve. This contradicts step [](#integral){.pf-ref}, which gives $2\pi i$. Hence no such $f$ exists and the statement is disproved. Equivalently, a holomorphic function on $U$ has a holomorphic primitive exactly when its integral over every closed curve in $U$ vanishes, and $2\pi i\neq0$ witnesses the failure.
:::

:::

:::

:::
