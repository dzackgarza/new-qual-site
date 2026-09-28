---
schema: qual/card@1
id: P-BERK90S-14
kind: problem
title: Dimension of endomorphisms preserving two subspaces whose sum is the whole space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the spanning hypothesis, both invariant subspaces, and both requested conclusions with Problem 14 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Decomposed V along the intersection of A and B and identified S with a direct sum of three spaces of linear maps.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked the direct-sum argument, the inverse to restriction, the dimension simplification, and the cases of zero-dimensional summands and coincident subspaces.
---

::: {.problem}
Let $A,B$ be subspaces of a finite-dimensional vector space $V$ with
$$
A+B=V.
$$
Write
$$
n=\dim V,
\qquad
a=\dim A,
\qquad
b=\dim B.
$$
Let $S$ be the set of endomorphisms $f$ of $V$ such that
$$
f(A)\subset A,
\qquad
f(B)\subset B.
$$
Prove that $S$ is a vector subspace of $\Endo(V)$, and express $\dim S$ in terms of $n,a,b$.
:::

::: {.hint}
Choose complements $U$ and $W$ to $A\cap B$ in $A$ and $B$,
respectively. Determine the possible restrictions of a map in $S$
to each summand of $V=(A\cap B)\oplus U\oplus W$.
:::

::: {.solution}
Let $K$ be the ground field, and put $C\coloneqq A\cap B$ and
$c\coloneqq\dim C$. All spaces of linear maps are taken over $K$.

<1>1. The set $S$ is a vector subspace of $\Endo(V)$.

::: {.proof}
The zero endomorphism belongs to $S$. Let $f,g\in S$ and
$\alpha,\beta\in K$. For every $x\in A$, the vectors $f(x)$
and $g(x)$ belong to $A$, so
$(\alpha f+\beta g)(x)=\alpha f(x)+\beta g(x)\in A$.
The same argument with $x\in B$ gives
$(\alpha f+\beta g)(x)\in B$. Thus $\alpha f+\beta g\in S$.
:::

<1>2. There are subspaces $U,W\subset V$ such that
$$
A=C\oplus U,\qquad B=C\oplus W,\qquad
V=C\oplus U\oplus W.
$$
Their dimensions satisfy $c=a+b-n$, $\dim U=a-c$, and
$\dim W=b-c$.

::: {.proof}
Extend a basis of $C$ to a basis of $A$ and to a basis of $B$.
Let $U$ and $W$ be the spans of the added basis vectors in $A$
and $B$, respectively. Then $A=C\oplus U$ and $B=C\oplus W$.
Since $A+B=V$, the subspaces $C,U,W$ span $V$.
Suppose $x+u+w=0$ with $x\in C$, $u\in U$, and $w\in W$.
Then $w=-(x+u)\in A\cap B=C$. Since $C\cap W=\{0\}$,
it follows that $w=0$; the equality $x+u=0$ and
$C\cap U=\{0\}$ give $x=u=0$. Thus the sum is direct.
Taking dimensions gives
$$
n=c+(a-c)+(b-c)=a+b-c,
$$
which proves all the asserted dimension identities.
:::

<1>3. Restriction gives a linear isomorphism
$$
\rho\colon S\longrightarrow
\Hom(C,C)\oplus\Hom(U,A)\oplus\Hom(W,B),
\qquad
\rho(f)=(f|_C,f|_U,f|_W).
$$

::: {.proof}
For $f\in S$ and $x\in C$, the vector $f(x)$ belongs to both
$A$ and $B$, hence to $C$. Also $f(U)\subset A$ and
$f(W)\subset B$. Therefore $\rho$ has the displayed codomain,
and restriction is linear.
Conversely, let $g_C\colon C\to C$, $g_U\colon U\to A$, and
$g_W\colon W\to B$ be linear maps. By step <1>2, there is a
unique linear map $f\colon V\to V$ defined by
$$
f(x+u+w)\coloneqq g_C(x)+g_U(u)+g_W(w)
\quad(x\in C,\ u\in U,\ w\in W).
$$
For $x+u\in A=C\oplus U$, its image is in $A$; for
$x+w\in B=C\oplus W$, its image is in $B$. Hence $f\in S$.
This construction is inverse to $\rho$, which proves the claim.
:::

<1>4. The requested dimension is
$$
\dim S=\boxed{n^2-a(n-a)-b(n-b)}.
$$

::: {.proof}
For finite-dimensional vector spaces $E,F$, choosing bases
identifies $\Hom(E,F)$ with the space of matrices with
$\dim F$ rows and $\dim E$ columns. Thus its dimension is
$(\dim E)(\dim F)$. Steps <1>2 and <1>3 give
$$
\begin{aligned}
\dim S
&=c^2+a(a-c)+b(b-c)\\
&=a^2+b^2+c\bigl(c-a-b\bigr)\\
&=a^2+b^2-n(a+b-n)\\
&=n^2-a(n-a)-b(n-b).
\end{aligned}
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves that $S$ is a subspace, and step <1>4 gives
its dimension in terms of $n,a,b$.
:::
:::
