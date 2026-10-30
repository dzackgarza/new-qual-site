---
schema: qual/card@1
id: P-VUTDR
kind: problem
title: Examples of a PID, a UFD, a torsion-free module, and a vanishing tensor product
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Principal Ideal Domains
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked all four example requests in June 2010 Rings and Modules 1 on PDF page 14; retained the source's optional-justification wording and corrected the area to algebra."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked ideal generation in Z, nonprincipality of (2,x), the divisibility obstruction to freeness of Q, and vanishing of every elementary tensor for two nonzero modules."
---
::: {.problem}
Give an example of each of the following.
Justification is not necessary.

(a) A principal ideal domain $D$ that is not a field.

(b) A unique factorization domain $D$ that is not a principal ideal domain.

(c) A commutative ring $R$, and a torsion-free $R$-module $M$, such that $M$ is not a free $R$-module.

(d) A commutative ring $R$, and two non-trivial $R$-modules $M$ and $N$ such that $M \otimes_R N \cong \{0\}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For part (a), take $D=\ZZ$.

::: pf-proof

The integers form an integral domain. A nonzero ideal $I$
contains a positive integer; let $d$ be its least positive
element. For $a\in I$, Euclidean division writes
$a=qd+r$ with $0\leq r<d$. Since $r=a-qd\in I$,
minimality implies $r=0$. Hence $I=(d)$. The zero ideal
is also principal, so $\ZZ$ is a PID. It is not a
field, because $2$ has no multiplicative inverse in $\ZZ$.

:::

:::

::: {.pf-step #s2}

For part (b), take $D=\ZZ[x]$.

::: pf-proof

The integers are a UFD, and the polynomial ring over a
UFD is a UFD by Gauss's lemma [@DF04]. Thus $D$ is a UFD.
The ideal $I=(2,x)$ is proper: the homomorphism
$\ZZ[x]\to\FF_2$, $f\mapsto f(0)\bmod2$,
annihilates both generators but does not annihilate $1$.

Suppose $I=(h)$. Since $h$ divides the nonzero constant
$2$, degree additivity in the domain $\ZZ[x]$
forces $h$ to be a nonzero integer. Since it also divides
$x$, comparison of the coefficient of $x$ in $x=hu(x)$
shows that $h$ divides $1$. Thus $h$ is a unit, which
would imply $I=D$, contradicting properness. Therefore
$D$ is not a PID.

:::

:::

::: {.pf-step #s3}

For part (c), take $R=\ZZ$ and $M=\QQ$.

::: pf-proof

For $0\ne n\in\ZZ$, the equation $nq=0$ in
$\QQ$ implies $q=0$, so $M$ is torsion-free.
But $2M=M$, since $q=2(q/2)$ for every rational $q$.
In a nonzero free $\ZZ$-module, a basis vector
cannot lie in twice the module: every coefficient in
the basis expansion of $2v$ is even, whereas that basis
vector has coefficient one at itself. Since $\QQ$
is nonzero and equals twice itself, it cannot be free.

:::

:::

::: {.pf-step #s4}

For part (d), take
$R=\ZZ$, $M=\ZZ/2\ZZ$, and
$N=\ZZ/3\ZZ$.

::: pf-proof

Both modules are nonzero. For any elementary tensor
$t=a\otimes b$, the tensor relations give
$2t=(2a)\otimes b=0$ and $3t=a\otimes(3b)=0$.
Therefore $t=(3-2)t=0$. Every element of the tensor
product is a finite sum of elementary tensors, so the
whole tensor product is zero, as required.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} answer parts (a)--(d), respectively.

:::

:::

:::
