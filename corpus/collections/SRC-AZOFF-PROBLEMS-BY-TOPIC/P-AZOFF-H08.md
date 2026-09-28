---
schema: qual/card@1
id: P-AZOFF-H08
kind: problem
title: Zeros of the exponential partial sums $P_n$ and $P_n-1$ in a disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the OCR-garbled radius to |z| < 10 and cleaned the LaTeX against Rouché’s theorem, Problem 8, of Azoff Problems by Topic.pdf (pdftotext layer reads |z| < 10).
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used uniform convergence of the exponential partial sums on |z|<=10.
    Rouché against exp(z) gives no zeros of P_n for all sufficiently large
    n. Rouché against exp(z)-1 gives the same zero count as its three zeros
    0 and +/-2pi i inside |z|<10.
---

::: {.problem}
For each integer $n \ge 1$, let $P_n(z) = 1 + z + \frac{1}{2!}z^2 + \frac{1}{3!}z^3 + \cdots + \frac{1}{n!}z^n$. Show that all sufficiently large $n$, the polynomial $P_n$ has no zeros in $\abs{z} < 10$, while the polynomial $P_n(z) - 1$ has exactly 3 zeros there.
:::

::: {.solution}
For
$$
P_n(z)=\sum_{k=0}^{n}\frac{z^k}{k!},
$$
write the exponential tail as
$$
R_n(z)
=
e^z-P_n(z)
=
\sum_{k=n+1}^{\infty}\frac{z^k}{k!}.
$$

<1>1. One has
$$
\sup_{\abs{z}\leq10}\abs{R_n(z)}
\longrightarrow0
$$
as $n\to\infty$.

::: {.proof}
For $\abs{z}\leq10$,
$$
\abs{R_n(z)}
\leq
\sum_{k=n+1}^{\infty}\frac{10^k}{k!}.
$$
The numerical series
$$
\sum_{k=0}^{\infty}\frac{10^k}{k!}
=
e^{10}
$$
converges, so its tails tend to zero. The bound is independent of $z$.
:::

<1>2. On the circle $\abs{z}=10$,
$$
\abs{e^z}\geq e^{-10}.
$$

::: {.proof}
If $\abs{z}=10$, then
$$
\operatorname{Re}z\geq-10.
$$
Therefore
$$
\abs{e^z}
=
e^{\operatorname{Re}z}
\geq
e^{-10}.
$$
:::

<1>3. For all sufficiently large $n$, the polynomial $P_n$ has no zeros in
$\abs{z}<10$.

::: {.proof}
By step <1>1, choose $N_1$ such that for every $n\geq N_1$,
$$
\sup_{\abs{z}\leq10}\abs{R_n(z)}
<
e^{-10}.
$$
Then on $\abs{z}=10$, steps <1>1 and <1>2 give
$$
\abs{P_n(z)-e^z}
=
\abs{R_n(z)}
<
\abs{e^z}.
$$
Rouché's theorem implies that $P_n$ and $e^z$ have the same number of zeros
in $\abs{z}<10$. The exponential has no zeros, so $P_n$ has none.
:::

<1>4. The zeros of $e^z-1$ in $\abs{z}<10$ are exactly
$$
0,
\qquad
2\pi i,
\qquad
-2\pi i,
$$
and each is simple.

::: {.proof}
The equation
$$
e^z=1
$$
has precisely the solutions
$$
z=2\pi i k,
\qquad
k\in\ZZ.
$$
The condition
$$
\abs{2\pi k}<10
$$
holds exactly for $k=0,\pm1$, since
$$
2\pi<10<4\pi.
$$
Moreover,
$$
\frac{d}{dz}(e^z-1)=e^z,
$$
which equals $1$ at every zero, so all three are simple.
:::

<1>5. There is a number $m>0$ such that
$$
\abs{e^z-1}\geq m
$$
for every $z$ with $\abs{z}=10$.

::: {.proof}
By step <1>4, none of the zeros of $e^z-1$ lies on the circle
$\abs{z}=10$. Thus the continuous positive function
$$
z\longmapsto\abs{e^z-1}
$$
has a strictly positive minimum $m$ on that compact circle.
:::

<1>6. For all sufficiently large $n$, the polynomial $P_n-1$ has exactly
three zeros in $\abs{z}<10$, counting multiplicity.

::: {.proof}
By step <1>1, choose $N_2$ such that for every $n\geq N_2$,
$$
\sup_{\abs{z}\leq10}\abs{R_n(z)}
<
m,
$$
where $m$ is from step <1>5. On $\abs{z}=10$,
$$
\begin{aligned}
\abs{
(P_n(z)-1)-(e^z-1)
}
&=
\abs{P_n(z)-e^z}\\
&=
\abs{R_n(z)}\\
&<
\abs{e^z-1}.
\end{aligned}
$$
Rouché's theorem implies that $P_n-1$ and $e^z-1$ have the same number of
zeros in the disk. Step <1>4 shows that this number is three.
:::

<1>7. For every
$$
n\geq\max\{N_1,N_2\},
$$
$P_n$ has no zeros in $\abs{z}<10$, while $P_n-1$ has exactly three zeros
there.

::: {.proof}
This combines steps <1>3 and <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required eventual zero-count statement.
:::
:::
