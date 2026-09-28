---
schema: qual/card@1
id: P-BKS09-8B
kind: problem
title: Centers of nonabelian groups and $p$-groups; groups of order $p^2$ are abelian
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared all three parts with the Spring 2009 solution-packet extraction and independently reviewed the quotient-center and class-equation arguments.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the cyclic quotient lemma, the p-divisibility of the center, and the order-p-squared conclusion.
---

::: {.problem}
1. Let G be a non-abelian finite group.
   Show that $G / Z ( G )$ is not cyclic, where $Z ( G )$ is the center of G.

2. If $| G | = p ^ { n }$ , with p prime and $n > 0$ , show that $Z ( G )$ is not trivial.

3. If $| G | = p ^ { 2 }$ , show that G is abelian.
:::

::: {.solution}
<1>1. If $G/Z(G)$ is cyclic, then $G$ is abelian.

::: {.proof}
Suppose
$$
G/Z(G)=\langle gZ(G)\rangle.
$$
For arbitrary $x,y\in G$, there exist integers $r,s$ and central elements
$z_1,z_2\in Z(G)$ such that
$$
x=g^rz_1,
\qquad
y=g^sz_2.
$$
Since $z_1$ and $z_2$ commute with every element of $G$,
$$
xy
=
g^{r+s}z_1z_2
=
g^{r+s}z_2z_1
=
yx.
$$
Thus every pair of elements of $G$ commutes.
:::

<1>2. If $G$ is nonabelian, then $G/Z(G)$ is not cyclic.

::: {.proof}
This is the contrapositive of step <1>1, and proves part 1.
:::

<1>3. If $\abs G=p^n$ with $n>0$, then
$$
p\mid\abs{Z(G)}.
$$

::: {.proof}
For $x\in G$, the conjugacy class of $x$ has cardinality
$$
[G:C_G(x)].
$$
This index divides $\abs G=p^n$, so every conjugacy-class size is a power
of $p$. The class has size $1$ exactly when $x\in Z(G)$. Hence every
noncentral conjugacy class has size divisible by $p$.

The class equation therefore has the form
$$
\abs G
=
\abs{Z(G)}
+
\sum_j p^{r_j},
\qquad
r_j\geq1.
$$
Reducing modulo $p$ and using $p\mid\abs G$ gives
$$
\abs{Z(G)}\equiv0\pmod p.
$$
:::

<1>4. If $\abs G=p^n$ with $n>0$, then $Z(G)$ is nontrivial.

::: {.proof}
The identity element lies in $Z(G)$, so $\abs{Z(G)}>0$. By step <1>3,
this positive integer is divisible by $p$, hence
$$
\abs{Z(G)}\geq p>1.
$$
This proves part 2.
:::

<1>5. If $\abs G=p^2$, then $G$ is abelian.

::: {.proof}
By step <1>4, the center has order divisible by $p$. Since its order also
divides $p^2$, either
$$
\abs{Z(G)}=p
$$
or
$$
\abs{Z(G)}=p^2.
$$
In the second case, $Z(G)=G$, so $G$ is abelian.

In the first case,
$$
\abs{G/Z(G)}=p.
$$
Every group of prime order is cyclic, so $G/Z(G)$ is cyclic. Step <1>1
then implies that $G$ is abelian. This proves part 3.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 proves part 1, step <1>4 proves part 2, and step <1>5 proves
part 3.
:::
:::
