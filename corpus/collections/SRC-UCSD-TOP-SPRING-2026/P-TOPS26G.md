---
schema: qual/card@1
id: P-TOPS26G
kind: problem
title: Cohomology ring of $\mathbb{CP}^n$ and orientation under homotopy equivalences
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
---

::: {.problem}
Compute the cohomology ring of $\mathbb{CP}^n$.
Show the following statements are equivalent:

- $n$ is even

- there is an orientation on $\mathbb{CP}^n$ that is preserved by every homotopy equivalence $f \colon \mathbb{CP}^n \to \mathbb{CP}^n$.
:::

::: {.solution}
<1>1. The integral cohomology ring is
$$\boxed{H^*(\mathbb{CP}^n;\mathbb Z)\cong\mathbb Z[x]/(x^{n+1}),\qquad |x|=2.}$$
::: {.proof}
This is the standard projective-space computation; $x$ is the first Chern class of the dual tautological line bundle.
:::

<1>2. Any homotopy equivalence $f:\mathbb{CP}^n\to\mathbb{CP}^n$ satisfies $f^*x=\pm x$.
::: {.proof}
The group $H^2\cong\mathbb Z$, and a cohomology isomorphism must send its generator to a generator.
:::

<1>3. On top cohomology,
$$f^*(x^n)=(\pm1)^n x^n.$$
::: {.proof}
Pullback is a ring homomorphism.
:::

<1>4. If $n$ is even, every homotopy equivalence preserves the complex orientation (and hence that orientation has the required property).
::: {.proof}
Then $(\pm1)^n=1$, so every $f^*$ fixes the chosen top generator $x^n$.
:::

<1>5. If $n$ is odd, complex conjugation $c:\mathbb{CP}^n\to\mathbb{CP}^n$ is a homotopy equivalence with $c^*x=-x$, hence $c^*(x^n)=-x^n$.
::: {.proof}
Conjugation is a homeomorphism and sends the first Chern class of a complex line bundle to its negative.
:::

<1>6. Thus when $n$ is odd no choice of orientation can be preserved by every homotopy equivalence, while when $n$ is even the complex orientation is. Therefore the two stated conditions are equivalent.
::: {.proof}
Changing the chosen orientation only replaces the top generator by its negative; an orientation-reversing self-equivalence reverses either choice.
:::
:::
