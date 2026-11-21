---
schema: qual/card@1
id: P-P3GIM
kind: problem
title: 'Fitting''s lemma: $V=U\oplus W$ with $\phi\restrict_U$ nilpotent and $\phi\restrict_W$ nonsingular'
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Eleven steps asserted their claim with no
    justification and each now carries one: the finiteness of the dimension, the inclusion of consecutive
    kernels and the reverse inclusion of consecutive images, the monotone bounded dimension sequence, the
    stabilization index with the passage from equal dimensions to equal subspaces, the definition of $U$
    and $W$ as kernel and image, the two invariance computations, the triviality of the intersection using
    stabilization at $2k$, the direct sum from rank--nullity, the nilpotence of the restriction to $U$,
    and the invertibility of the restriction to $W$ through its vanishing kernel. The closing step now
    states the Fitting decomposition with its own proof, in place of a pf-qed that only pointed at steps
    2, 3 and 4. One display was orphaned outside the step whose claim introduced it, so the claim now
    carries the identity and the display is gone. Sources are cited by numbered statement: the
    rank--nullity theorem, and the characterization of an invertible endomorphism of a
    finite-dimensional space by a trivial kernel. No page reference is written in the body of this card or
    in the event above. The statement is unchanged. The collection retains the UGA algebra qualifying
    exam of Fall 2018 and no solution sheet, so the argument is the card's own.
---
::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $F$, and let $\phi: V \to V$ be a linear transformation.

Prove that there exists a direct sum decomposition
$$
V = U \oplus W,
$$
where $U$ and $W$ are $\phi$-invariant subspaces of $V$, $\phi\restrict_U$ is nilpotent, and $\phi\restrict_W$ is invertible (nonsingular).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For some $k\geq1$, the kernels of all powers $\phi^j$ with $j\geq k$ equal $\ker(\phi^k)$.

::: pf-proof

::: pf-step

Let $n = \dim_F V < \infty$.


::: pf-proof
$V$ is finite-dimensional over $F$, so it has a dimension $n$, a non-negative integer, and every subspace of $V$ has dimension at most $n$; the number $n$ is fixed once and for all in what follows.
:::

:::

::: pf-step

Consider the ascending chain of kernels and the descending chain of images:
    $$\ker(\phi) \subseteq \ker(\phi^2) \subseteq \ker(\phi^3) \subseteq \cdots \subseteq V,$$
    $$V \supseteq \operatorname{Im}(\phi) \supseteq \operatorname{Im}(\phi^2) \supseteq \operatorname{Im}(\phi^3) \supseteq \cdots$$


::: pf-proof
Powers of a linear map are linear, so $\ker(\phi^m)$ is a subspace. If $\phi^m(v) = 0$ then $\phi^{m+1}(v) = \phi(0) = 0$, which gives the inclusion $\ker(\phi^m) \subseteq \ker(\phi^{m+1})$; dually $\operatorname{Im}(\phi^{m+1}) = \phi(\operatorname{Im}(\phi^m)) \subseteq \operatorname{Im}(\phi^m)$, so the first chain ascends and the second descends.
:::

:::

::: pf-step

Because $\dim_F V = n < \infty$, the sequence of dimensions $\dim_F \ker(\phi^m)$ is non-decreasing and bounded above by $n$.


::: pf-proof
The dimensions $\dim_F\ker(\phi^m)$ form a non-decreasing sequence of integers by the ascending chain of the previous step, and each is at most $\dim_F V = n$ because a subspace of $V$ has dimension at most that of $V$.
:::

:::

::: pf-step

Thus the chain of kernels must stabilize: there exists an integer $k \le n$ such that
    $$\ker(\phi^k) = \ker(\phi^{k+1}) = \ker(\phi^{k+2}) = \cdots = \ker(\phi^{2k}).$$


::: pf-proof
A non-decreasing sequence of integers all lying in $\{0, 1, \dots, n\}$ can increase at most $n$ times, so there is some $k \le n$ with $\dim_F\ker(\phi^k) = \dim_F\ker(\phi^{k+1})$. The inclusion $\ker(\phi^k) \subseteq \ker(\phi^{k+1})$ together with equality of dimensions makes the two subspaces equal, and repeating the argument gives $\ker(\phi^j) = \ker(\phi^k)$ for every $j \ge k$, in particular for $j = 2k$ because $2k \ge k$.
:::

:::

::: pf-step

Set $U = \ker(\phi^k)$ and $W = \operatorname{Im}(\phi^k)$; both are subspaces of $V$.


::: pf-proof
The kernel and the image of a linear map are subspaces, and $\phi^k$ is linear as a composite of linear maps, so $U$ and $W$ are subspaces of $V$.
:::

:::

:::

:::

::: {.pf-step #s2}

The subspaces $U=\ker(\phi^k)$ and $W=\operatorname{im}(\phi^k)$ are $\phi$-invariant.

::: pf-proof

::: pf-step

For $u \in U = \ker(\phi^k)$:
    $$\phi^k(\phi(u)) = \phi(\phi^k(u)) = \phi(0) = 0,$$
    so $\phi(u) \in \ker(\phi^k) = U$.


::: pf-proof
Powers of one linear map commute, so $\phi^k(\phi(u)) = \phi^{k+1}(u) = \phi(\phi^k(u)) = \phi(0) = 0$ for $u \in \ker(\phi^k)$, which says $\phi(u)$ lies in $\ker(\phi^k)$; hence $U$ is carried into itself.
:::

:::

::: pf-step

For $w \in W = \operatorname{Im}(\phi^k)$ there is $v \in V$ with $w = \phi^k(v)$, and then $\phi(w) = \phi(\phi^k(v)) = \phi^k(\phi(v)) \in W$.


::: pf-proof
For $w = \phi^k(v)$ in the image of $\phi^k$ one has $\phi(w) = \phi(\phi^k(v)) = \phi^k(\phi(v))$, which is the image under $\phi^k$ of the vector $\phi(v)$ and so lies in $\operatorname{Im}(\phi^k)$; hence $W$ is carried into itself.
:::

:::

:::

:::

::: {.pf-step #s3}

The vector space decomposes as $V=U\oplus W$.

::: pf-proof

::: pf-step

$U \cap W = \{0\}$.
        - Let $v \in U \cap W$.
        - Since $v \in W = \operatorname{Im}(\phi^k)$, there exists $x \in V$ such that $v = \phi^k(x)$.
        - Since $v \in U = \ker(\phi^k)$, $\phi^k(v) = 0$, which gives $\phi^{2k}(x) = 0$.
        - Thus $x \in \ker(\phi^{2k})$.
        - By stabilization at index $k$ (step [](#s1){.pf-ref}), $\ker(\phi^{2k}) = \ker(\phi^k)$, so $x \in \ker(\phi^k)$.
        - Therefore $v = \phi^k(x) = 0$.
        - Hence $U \cap W = \{0\}$.


::: pf-proof
Let $v \in U \cap W$. Since $v$ is in the image of $\phi^k$ there is $x \in V$ with $v = \phi^k(x)$, and since $v$ is in the kernel of $\phi^k$ we get $0 = \phi^k(v) = \phi^{2k}(x)$, so $x \in \ker(\phi^{2k})$. By the stabilization of step [](#s1){.pf-ref} the kernel at $2k$ equals the kernel at $k$, so $x \in \ker(\phi^k)$ and $v = \phi^k(x) = 0$. Hence the intersection is $\{0\}$.
:::

:::

::: pf-step

$V = U + W$.


::: pf-proof
The rank--nullity theorem applied to the linear map $\phi^k \colon V \to V$ gives $\dim_F U + \dim_F W = n$. For subspaces with trivial intersection the dimension of the sum is the sum of the dimensions, so $\dim_F(U + W) = n = \dim_F V$; a subspace of $V$ with the dimension of $V$ is all of $V$, so $V = U + W$.
:::

:::

- By the Rank-Nullity Theorem applied to the linear map $\phi^k: V \to V$:
$$\dim_F \ker(\phi^k) + \dim_F \operatorname{Im}(\phi^k) = \dim_F V.$$
- Since $U \cap W = \{0\}$, $\dim_F(U \oplus W) = \dim_F U + \dim_F W = \dim_F V$.
- A subspace of $V$ with the same finite dimension as $V$ must be $V$ itself.
- Thus $V = U \oplus W$.

:::

:::

::: {.pf-step #s4}

The restriction $\phi\restrict_U$ is nilpotent, while $\phi\restrict_W$ is invertible.

::: pf-proof

::: pf-step

$\phi\restrict_U$ is nilpotent.
        - For every $u \in U = \ker(\phi^k)$, $(\phi\restrict_U)^k(u) = \phi^k(u) = 0$.
        - Thus $(\phi\restrict_U)^k = 0$, so $\phi\restrict_U$ is nilpotent.


::: pf-proof
For $u \in U$ one has $(\phi\restrict_U)^k(u) = \phi^k(u) = 0$ because $U = \ker(\phi^k)$, so the $k$-th power of the restriction is the zero map and the restriction is nilpotent.
:::

:::

::: pf-step

$\phi\restrict_W$ is invertible.


::: pf-proof
An endomorphism of a finite-dimensional space is invertible exactly when its kernel is trivial, by rank--nullity. If $w \in W$ satisfies $\phi(w) = 0$ then $\phi^k(w) = \phi^{k-1}(\phi(w)) = 0$, so $w \in \ker(\phi^k) = U$, and $w \in U \cap W = \{0\}$ by step [](#s3){.pf-ref}; hence the kernel of the restriction is trivial and the restriction is invertible.
:::

:::

- Since $W$ is finite-dimensional, $\phi\restrict_W: W \to W$ is invertible if and only if $\ker(\phi\restrict_W) = \{0\}$.
- Let $w \in \ker(\phi\restrict_W)$. Then $w \in W$ and $\phi(w) = 0$.
- Then $\phi^k(w) = \phi^{k-1}(\phi(w)) = \phi^{k-1}(0) = 0$, so $w \in \ker(\phi^k) = U$.
- Thus $w \in U \cap W$.
- By step [](#s3){.pf-ref}, $U \cap W = \{0\}$, so $w = 0$.
- Therefore $\ker(\phi\restrict_W) = \{0\}$, which proves that $\phi\restrict_W$ is invertible.

:::

:::

::: pf-step
$V = U \oplus W$ with $U$ and $W$ $\phi$-invariant, $\phi\restrict_U$ nilpotent and $\phi\restrict_W$ invertible.

::: pf-proof
Step [](#s1){.pf-ref} produces the index $k$ at which the kernels stabilize and defines $U$ and $W$ from it; step [](#s2){.pf-ref} shows both are carried into themselves by $\phi$; step [](#s3){.pf-ref} gives $U \cap W = \{0\}$ together with $V = U + W$, which is the direct sum; and step [](#s4){.pf-ref} gives the nilpotence of one restriction and the invertibility of the other. Those are exactly the four clauses the decomposition is required to satisfy.
:::

:::

:::
:::
