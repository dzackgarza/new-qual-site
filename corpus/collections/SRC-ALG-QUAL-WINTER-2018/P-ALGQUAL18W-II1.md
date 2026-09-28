---
schema: qual/card@1
id: P-ALGQUAL18W-II1
kind: problem
title: Proper subgroups of $S_n$ of order greater than $(n-1)!$
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 1 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Independently proved the n>=5 case from the coset action and simplicity of
    A_n, then handled n<=4 explicitly. The resulting classification agrees
    with the recorded source solution: A_n for n>=3, plus the three Sylow
    2-subgroups of S_4.
---

::: {.problem}
Describe all proper subgroups of $S_n$ whose order is strictly greater than $(n-1)!$.
:::

::: {.solution}
Let
$$
H<S_n
$$
be proper and suppose
$$
\abs{H}>(n-1)!.
$$
Put
$$
m=[S_n:H].
$$

<1>1. The index $m$ satisfies
$$
2\leq m<n.
$$

::: {.proof}
Since $H$ is proper,
$$
m\geq2.
$$
Also
$$
m
=
\frac{n!}{\abs H}
<
\frac{n!}{(n-1)!}
=
n.
$$
:::

<1>2. The action of $S_n$ on the left cosets $S_n/H$ gives a nontrivial
homomorphism
$$
\rho:S_n\longrightarrow S_m.
$$

::: {.proof}
Left multiplication permutes the $m$ cosets, giving the homomorphism
$\rho$.

The action is transitive. Since $m\geq2$ by step <1>1, a transitive action
on $m$ points is not trivial. Hence $\rho$ is nontrivial.
:::

<1>3. Assume $n\geq5$. Then the restriction
$$
\rho|_{A_n}:A_n\longrightarrow S_m
$$
is trivial.

::: {.proof}
For $n\geq5$, the alternating group $A_n$ is simple.

If the restriction were nontrivial, simplicity would make its kernel
trivial, so it would be injective. This would force
$$
\abs{A_n}
\leq
\abs{S_m}
=
m!.
$$
But step <1>1 gives
$$
m\leq n-1,
$$
and therefore
$$
m!
\leq
(n-1)!
<
\frac{n!}{2}
=
\abs{A_n},
$$
where the strict middle inequality uses $n\geq5$. Contradiction.

Thus $\rho|_{A_n}$ is trivial.
:::

<1>4. If $n\geq5$, then
$$
\boxed{H=A_n.}
$$

::: {.proof}
By step <1>3,
$$
A_n\subseteq\ker\rho.
$$
Hence the coset action factors through
$$
S_n/A_n\cong C_2.
$$
The induced $C_2$-action on $S_n/H$ is still transitive. Every transitive
orbit of a group of order $2$ has size at most $2$, so
$$
m\leq2.
$$
Step <1>1 gives $m\geq2$, hence
$$
m=2.
$$

Thus $H$ has index $2$. Since $A_n\subseteq\ker\rho\subseteq H$ and both
$A_n$ and $H$ have index $2$ in $S_n$, they have the same order. Therefore
$$
H=A_n.
$$
:::

<1>5. For every $n\geq3$, the subgroup $A_n$ satisfies the required
inequality.

::: {.proof}
The subgroup $A_n$ is proper of order
$$
\abs{A_n}
=
\frac{n!}{2}.
$$
For $n\geq3$,
$$
\frac{n!}{2}
>
(n-1)!
\quad\Longleftrightarrow\quad
\frac n2>1,
$$
which holds. Hence $A_n$ is always an example for $n\geq3$.
:::

<1>6. For $n=1$ and $n=2$, there are no such proper subgroups.

::: {.proof}
For $n=1$,
$$
\abs{S_1}=1=(1-1)!,
$$
so no subgroup can have order strictly greater than $(n-1)!$.

For $n=2$,
$$
(n-1)!=1.
$$
The only proper subgroup of $S_2$ is the trivial subgroup, of order $1$,
which does not satisfy the strict inequality.
:::

<1>7. For $n=3$, the unique possibility is
$$
\boxed{H=A_3.}
$$

::: {.proof}
Here
$$
(n-1)!=2.
$$
A proper subgroup of $S_3$ has order dividing $6$ and strictly less than
$6$. The only divisor strictly greater than $2$ is $3$. Thus
$$
\abs H=3.
$$
The unique subgroup of order $3$ is the Sylow $3$-subgroup
$$
A_3.
$$
:::

<1>8. For $n=4$, any such subgroup has order $8$ or $12$.

::: {.proof}
Now
$$
(n-1)!=6.
$$
By Lagrange's theorem, the order of a proper subgroup divides
$$
\abs{S_4}=24
$$
and is strictly between $6$ and $24$. The only possibilities are
$$
8
\quad\text{and}\quad
12.
$$
:::

<1>9. The unique subgroup of $S_4$ of order $12$ is
$$
A_4.
$$

::: {.proof}
A subgroup of order $12$ has index $2$, hence is normal. Every index-two
subgroup is the kernel of a surjective homomorphism
$$
S_4\longrightarrow C_2.
$$
The commutator subgroup of $S_4$ is $A_4$, so every homomorphism to an
abelian group kills $A_4$. Hence
$$
A_4\subseteq H.
$$
Both groups have order $12$, so
$$
H=A_4.
$$
:::

<1>10. The subgroups of $S_4$ of order $8$ are exactly three Sylow
$2$-subgroups.

::: {.proof}
An order-$8$ subgroup is a Sylow $2$-subgroup because
$$
24=2^3\cdot3.
$$

There are three partitions of
$$
\{1,2,3,4\}
$$
into two unordered pairs:
$$
\{12\mid34\},
\qquad
\{13\mid24\},
\qquad
\{14\mid23\}.
$$
For each partition, its setwise stabilizer in $S_4$ has order
$$
2\cdot2\cdot2=8:
$$
one may swap the two entries inside either pair and may swap the two pairs.
Thus these are three distinct Sylow $2$-subgroups.

Sylow's theorem says the number $n_2$ of Sylow $2$-subgroups divides $3$
and satisfies
$$
n_2\equiv1\pmod2.
$$
Hence
$$
n_2\in\{1,3\}.
$$
Since we have exhibited three distinct ones,
$$
n_2=3.
$$
:::

<1>11. The complete classification is:
$$
\boxed{
\begin{aligned}
&\text{no examples}, && n=1,2;\\
&A_n, && n\geq3;\\
&\text{the three Sylow }2\text{-subgroups of }S_4,
&&\text{additionally when }n=4.
\end{aligned}
}
$$

::: {.proof}
Steps <1>3--<1>5 classify all cases $n\geq5$ and verify $A_n$ as an example
for every $n\geq3$. Steps <1>6--<1>10 exhaust the small cases.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 gives all proper subgroups satisfying the required order bound.
:::
:::
