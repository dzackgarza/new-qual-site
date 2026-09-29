---
schema: qual/card@1
id: P-AGH2412VALEX
kind: problem
title: Valuation rings of function fields of dimension one and two
classification:
  areas:
  - algebraic-geometry
  topics:
  - Valuation Rings
  - Function Fields
  - Blowing Up
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against Hartshorne II.4.12 and the later surface-valuation classification. The second surface example needs normality at the generic point of the contracted curve; this correction is recorded below.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: Replaced the discreteness tautology by a proved formal-arc criterion, justified both examples and the normality counterexample, and repaired the citations and structured-proof presentation.
---

::: {.problem}
Let $k$ be an algebraically closed field.

(a) If $K$ is a function field of dimension $1$ over $k$, then every valuation ring of $K/k$ except $K$ itself is discrete.
    Thus the set of all of them is just the abstract nonsingular curve $C_K$ of (I, §6).

(b) If $K/k$ is a function field of dimension two, there are several different kinds of valuations.
    Suppose that $X$ is a complete nonsingular surface with function field $K$.

- If $Y$ is an irreducible curve on $X$ with generic point $x_1$, then the local ring $R = \OO_{x_1, X}$ is a discrete valuation ring of $K/k$ with center at the nonclosed point $x_1$ on $X$.

- If $f: X' \to X$ is a birational morphism, and if $Y'$ is an irreducible curve in $X'$ whose image in $X$ is a single closed point $x_0$, then the local ring $R$ of the generic point of $Y'$ on $X'$ is a discrete valuation ring of $K/k$ with center at the closed point $x_0$ on $X$.

- Let $x_0 \in X$ be a closed point.
  Let $f: X_1 \to X$ be the blowing-up of $x_0$ (I, §4) and let $E_1 = \inverseof{f}(x_0)$ be the exceptional curve.
  Choose a closed point $x_1 \in E_1$, let $f_2: X_2 \to X_1$ be the blowing-up of $x_1$, and let $E_2 = \inverseof{f_2}(x_1)$ be the exceptional curve.
  Repeat.

  In this way we obtain a sequence of varieties $X_i$ with closed points $x_i$ chosen on them, and for each $i$ the local ring $\OO_{x_{i+1}, X_{i+1}}$ dominates $\OO_{x_i, X_i}$.
  Let $R_0 = \bigcup_{i \geq 0} \OO_{x_i, X_i}$.
  Then $R_0$ is a local ring, so it is dominated by some valuation ring $R$ of $K/k$ by (I, 6.1A).

  Show that $R$ is a valuation ring of $K/k$, and that it has center $x_0$ on $X$.
  When is $R$ a discrete valuation ring?

Note: we will see later (V, Ex.
5.6) that in fact the $R_0$ of the third kind is already a valuation ring itself, so $R_0 = R$.
Furthermore, every valuation ring of $K/k$ except $K$ itself is one of the three kinds just described.
:::

::: {.solution}
For the third construction put $X_0=X$, $A_i=\OO_{X_i,x_i}$, and let $\mathfrak m_i$ be the maximal ideal of $A_i$.
All these rings are viewed inside $K$ through the birational maps.
The second construction is treated with $X'$ normal at the generic point of $Y'$, as justified in the erratum.

::: pf

::: {.pf-step #s1}

In part (a), every valuation ring $R\subsetneq K$ of $K/k$ is the local ring of a unique closed point on the nonsingular projective model of $K$.

::: pf-proof

Choose the nonsingular projective curve $C$ with function field $K$ [@Har10a, Chapter I, §6].
The valuative criterion for properness extends the generic-point map $\Spec K\to C$ uniquely to $\Spec R\to C$ [@Har10a, Theorem II.4.7].
If the image $x$ of the closed point were generic, domination would give $K=\OO_{C,x}\subseteq R$, contrary to $R\ne K$.
Thus $x$ is closed, and $\OO_{C,x}$ is a one-dimensional regular local ring, hence a DVR [@Har10a, Theorem I.6.2A].
A valuation ring dominating another valuation ring of the same field equals it [@Har10a, Theorem I.6.1A].
Consequently
$$
R=\OO_{C,x}.
$$
Conversely each such local ring is a valuation ring of $K/k$.
These are precisely the points in the abstract nonsingular curve $C_K$.

:::

:::

::: {.pf-step #s2}

The first two surface constructions give DVRs with the stated centers, under the corrected hypothesis in the second construction.

::: pf-proof

For the first construction, the generic point $x_1$ of $Y$ has codimension one in the nonsingular surface $X$.
Thus $\OO_{X,x_1}$ is a one-dimensional regular local domain with fraction field $K$, so is a DVR [@Har10a, Theorem I.6.2A].
It contains $k$ and dominates itself, giving center $x_1$.

For the second construction, write $\eta'$ for the generic point of $Y'$.
The local ring $\OO_{X',\eta'}$ is a one-dimensional noetherian local domain with fraction field $K$.
Normality at $\eta'$ makes it integrally closed, hence a DVR by the same theorem.
Since $f(\eta')=x_0$, the induced inclusion $\OO_{X,x_0}\hookrightarrow\OO_{X',\eta'}$ is local.
This is domination, so its center on $X$ is $x_0$.
In both cases $k^\times$ consists of units, so the valuation is trivial on $k$.

:::

:::

::: {.pf-step #s3}

The union $R_0$ is a local domain with maximal ideal $\mathfrak m_\infty=\bigcup_i\mathfrak m_i$ and residue field $k$.
Every valuation ring $R$ of $K$ dominating $R_0$ is a valuation ring of $K/k$ with center $x_0$.

::: pf-proof

A blowup of a nonsingular surface at a closed point is nonsingular [@Har10a, Proposition V.3.1].
Hence every $A_i$ is a two-dimensional regular local domain with fraction field $K$ and residue field $k$.
The maps $A_i\hookrightarrow A_{i+1}$ are local, so $\mathfrak m_{i+1}\cap A_i=\mathfrak m_i$.
An element outside $\mathfrak m_i$ is already a unit in $A_i$; an element in $\mathfrak m_i$ remains a nonunit in every later ring.
Thus $R_0$ is local with the stated maximal ideal.
For every $a\in A_i$ there is a unique $c\in k$ with $a-c\in\mathfrak m_i$, so $R_0/\mathfrak m_\infty\cong k$.

The domination theorem supplies a valuation ring $R\subset K$ dominating $R_0$ [@Har10a, Theorem I.6.1A].
It contains $k$, and every nonzero constant is a unit.
Moreover
$$
\mathfrak m_R\cap A_0=\mathfrak m_\infty\cap A_0=\mathfrak m_0.
$$
Thus $R$ dominates $\OO_{X,x_0}$ and has center $x_0$.
It is not a field, since $\mathfrak m_0\ne0$.

:::

:::

::: {.pf-step #s4}

If a DVR $V$ of $K$ dominates every $A_i$, then $V=R_0$.

::: pf-proof

Normalize its valuation as $v:K^\times\to\ZZ$.
For a nonzero $z\in V$, write $z=a_0/b_0$ with nonzero $a_0,b_0\in A_0$.
Suppose $z=a_i/b_i$ with $a_i,b_i\in A_i$.
If $b_i$ is a unit, then $z\in A_i$.
Otherwise $v(b_i)>0$, and $v(a_i)\ge v(b_i)$ implies $a_i,b_i\in\mathfrak m_i$.

Choose regular parameters $p_i,q_i$ in $A_i$.
The blowup has charts $A_i[q_i/p_i]$ and $A_i[p_i/q_i]$ [@Har10a, Chapter II, §7].
On either chart the extended ideal $(p_i,q_i)$ is generated by its denominator.
Thus $\mathfrak m_i A_{i+1}=(e_i)$ for a local equation $e_i$ of the exceptional curve.
Since $x_{i+1}$ lies on this curve, $e_i\in\mathfrak m_{i+1}$.
Set $a_{i+1}=a_i/e_i$ and $b_{i+1}=b_i/e_i$, which belong to $A_{i+1}$ and still have quotient $z$.
Then
$$
0\le v(b_{i+1})=v(b_i)-v(e_i)<v(b_i).
$$
These nonnegative integers cannot decrease indefinitely.
Eventually $v(b_N)=0$, so domination makes $b_N$ a unit of $A_N$ and $z\in A_N$.
This proves $V\subseteq R_0$; the reverse inclusion is assumed.

:::

:::

::: {.pf-step #s5}

The ring $R$ in the third construction is discrete precisely when there is a $k$-embedding $\iota:K\hookrightarrow k((t))$ such that, for every $i$,
$$
\iota(A_i)\subseteq k[[t]],
\qquad
\iota(\mathfrak m_i)\subseteq t k[[t]].
$$
For any such embedding,
$$
R=R_0=\boxed{\iota^{-1}(k[[t]])}.
$$
Geometrically, this says that the prescribed sequence is realized by the successive lifts of a formal arc $\Spec k[[t]]\to X$ whose generic point maps to the generic point of $X$.

::: pf-proof

::: {.pf-step #s5-1}

Discreteness implies the existence of this embedding.

::: pf-proof

Apply step [](#s4){.pf-ref} to $V=R$.
Then $R=R_0$ and its residue field is $k$ by step [](#s3){.pf-ref}. Choose a uniformizer $\pi\in R$.
The completion map $R\to\widehat R$ is injective, since a nonzero element has finite valuation and cannot belong to every $(\pi^n)$.
Every element of $\widehat R$ has a unique expansion $\sum_{n\ge0}c_n\pi^n$ with $c_n\in k$: subtract its residue, divide by $\pi$, and repeat, using completeness.
Thus $\widehat R\cong k[[t]]$ with $\pi$ corresponding to $t$.
Passing to fraction fields embeds $K$ into $k((t))$.
The inclusions of the $A_i$ into $R$ are local, giving the required conditions.

:::

:::

::: {.pf-step #s5-2}

Such an embedding implies discreteness.

::: pf-proof

Let $V=\iota^{-1}(k[[t]])$ and restrict the $t$-adic valuation to $K$.
Its value group is a nonzero subgroup of $\ZZ$: every nonzero element of $\mathfrak m_0$ has positive value.
A nonzero subgroup of $\ZZ$ is infinite cyclic, so $V$ is a DVR. For every $i$, units of $A_i$ map to units of $k[[t]]$, since both the unit and its inverse lie in $A_i$.
The stated condition on $\mathfrak m_i$ therefore says that $V$ dominates $A_i$.
By step [](#s4){.pf-ref}, $V=R_0$.
Since $R$ dominates the valuation ring $V$ inside the same field, $R=V$ [@Har10a, Theorem I.6.1A].

:::

:::

::: pf-qed

Steps [](#s5-1){.pf-ref} and [](#s5-2){.pf-ref} prove the equivalence and identify the ring.
The local maps $A_i\to k[[t]]$ give compatible morphisms $\Spec k[[t]]\to X_i$ centered at $x_i$; their maps on function fields are $\iota$.
Conversely such lifts induce these local maps.

:::

:::

:::

::: {.pf-step #s6}

Discrete valuations occur in the third construction, even though every center $x_i$ is closed.

::: pf-proof

Take $X=\PP_k^2$, with affine coordinates $x,y$, and put
$$
\phi(t)=\sum_{n\ge1}t^{n!}\in t k[[t]].
$$
This series is transcendental over $k(t)$.
Indeed, let $P(T,Z)\in k[T,Z]$ be nonzero and suppose $P(t,\phi(t))=0$.
For $\phi_N(t)=\sum_{n=1}^N t^{n!}$, the polynomial $P(t,\phi_N(t))$ is divisible by $t^{(N+1)!}$, whereas its degree is at most $\deg_T P+(\deg_Z P)N!$.
For all sufficiently large $N$ this degree is smaller than $(N+1)!$, so $P(t,\phi_N(t))=0$.
This gives infinitely many distinct roots $\phi_N\in k(t)$ of the nonzero polynomial $P(t,Z)$, a contradiction.

Consequently $x\mapsto t$, $y\mapsto\phi(t)$ defines a $k$-embedding $k(x,y)\hookrightarrow k((t))$.
The restricted valuation has value group $\ZZ$, since $v(x)=1$, and residue field $k$.
It defines a DVR $V$ centered at the origin.
At each successive blowup, properness gives a center of $V$ over the preceding center.
Its residue field embeds into $V/\mathfrak m_V=k$, so this center is a closed $k$-point.
This constructs an infinite sequence of the required form, all of whose local rings are dominated by $V$.
Step [](#s4){.pf-ref} identifies their union with $V$.

:::

:::

::: {.pf-step #s7}

Nondiscrete valuations also occur in the third construction.

::: pf-proof

Again take $X=\PP_k^2$ and $K=k(x,y)$.
For a nonzero polynomial $P=\sum c_{ab}x^a y^b$, define
$$
v(P)=\min\{(a,b):c_{ab}\ne0\}\in\ZZ^2_{\mathrm{lex}},
$$
and extend by $v(P/Q)=v(P)-v(Q)$.
The least monomial of a product is the product of the least monomials, so this is well-defined and multiplicative; the inequality for addition follows from the minimum.
Thus it is a valuation, trivial on $k$, with value group $\ZZ^2_{\mathrm{lex}}$.

At stage $i$ use coordinates $y,u_i=x/y^i$, starting with $u_0=x$.
Their values are $(0,1)$ and $(1,-i)$, both positive in lexicographic order.
The center is therefore the closed point $y=u_i=0$.
Blowing up that point and taking the chart $u_{i+1}=u_i/y$ repeats this construction, with the next center on the exceptional curve $y=0$.
The valuation ring dominates every $A_i$, hence their local union.
Its value group is not infinite cyclic, so it is not a DVR.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a). Step [](#s2){.pf-ref} proves the first two surface examples with the stated correction, and step [](#s3){.pf-ref} proves the domination and center assertions for the third.
Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} characterize when the third construction is discrete; steps [](#s6){.pf-ref} and [](#s7){.pf-ref} show that both possibilities occur.

:::

:::

:::

::: {.remark title="Erratum"}
The second example in part (b) requires $X'$ to be normal at the generic point of $Y'$.
An arbitrary birational morphism does not supply this hypothesis.

For a counterexample let $X=\PP_k^2$ and blow up the zero-dimensional subscheme supported at the affine origin with ideal $(x^2,y^2)$.
One affine chart of this birational model has coordinate ring
$$
B=k[x,y,s]/(y^2-sx^2)\subset k(x,y),\qquad s=y^2/x^2.
$$
The exceptional curve has generic prime $\mathfrak p=(x,y)$.
After inverting $k[s]\setminus\{0\}$, its local ring is
$$
B_{\mathfrak p}\cong
\bigl(k(s)[x,y]/(y^2-sx^2)\bigr)_{(x,y)}.
$$
This is a one-dimensional local domain: $s$ is not a square in $k(s)$, so the defining quadratic is irreducible.
Its maximal ideal has two independent classes $x,y$ modulo its square, since the defining relation has degree two.
Hence this local ring is not regular and is not a DVR [@Har10a, Theorem I.6.2A].
The exceptional curve is nevertheless contracted to the closed origin of $X$.
Normality at its generic point is therefore necessary for the asserted DVR conclusion, and Theorem I.6.2A makes it sufficient.
:::
