---
schema: qual/card@1
id: P-AGH334DEPTHCOH
kind: problem
title: Cohomological interpretation of depth
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Cohomology
  - Depth
  - Regular Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts and the associated-prime hint with the retained Hartshorne Chapter III section 3 transcription. Checked the finite-module depth convention against Stacks Project section 10.72. The induction uses only the long exact sequence and elementwise ideal torsion, and treats aM=M rather than discarding that case.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a noetherian ring and $\mfa$ an ideal.
For a finite $A$-module $M$ with $\mfa M\ne M$, let $\depth_\mfa M$ be the maximum length of an $M$-regular sequence in $\mfa$.
Use the convention $\depth_\mfa M=\infty$ when $M$ is finite and $\mfa M=M$, including $M=0$.
This generalizes the notion of depth introduced in (II, §8).

(a) For any $A$-module $M$, show that the existence of an $M$-regular element in $\mfa$ implies $\Gamma_{\mfa}(M)=0$.
For $M$ finitely generated, show that $\Gamma_{\mfa}(M)=0$ if and only if $\depth_\mfa M\ge1$, with the stated convention.

(b) Show inductively, for $M$ finitely generated, that for any $n\ge0$, the following conditions are equivalent:

(i) $\depth_{\mfa} M\ge n$;

(ii) $H_\mfa^i(M)=0$ for all $0\le i<n$.
:::

::: {.hint}
When $M$ is finitely generated, both conditions in (a) are equivalent to saying that $\mfa$ is not contained in any associated prime of $M$.
:::

::: {.solution}
Write $T^i(M)=H_{\mfa}^i(M)$ and $T^0(M)=\Gamma_{\mfa}(M)$.
By [[P-AGH333LOCALCOH]], every element of every $T^i(M)$ is killed by a power of $\mfa$.
Regular sequences have nonzero final quotient, and the finite-module depth convention is the one in [[D-DEFREGSQ]].

::: pf

::: {.pf-step #s1}

If multiplication by some $x\in\mfa$ is injective on $M$, then $T^0(M)=0$.

::: pf-proof

For $m\in T^0(M)$, choose $q\ge1$ with $\mfa^qm=0$.
Then $x^qm=0$.
A power of an injective endomorphism is injective, so $m=0$.
This proves the forward implication in (a) for arbitrary modules, and even when the injective multiplication map is surjective.

:::

:::

::: {.pf-step #s2}

For a finite module $M$, $T^0(M)=0$ exactly when $\mfa$ is contained in no associated prime of $M$.
When $\mfa M\ne M$, this is equivalent to the existence of an $M$-regular element in $\mfa$.

::: pf-proof

If $\mathfrak p=\Ann_A(m)$ for some $0\ne m\in M$ and $\mfa\subseteq\mathfrak p$, then $\mfa m=0$ and $T^0(M)\ne0$.
Conversely, if $T^0(M)\ne0$, choose an associated prime $\mathfrak p$ of this nonzero finite submodule.
Such a prime exists for a nonzero finite module over a noetherian ring.
It is the annihilator of a nonzero element $m\in T^0(M)$, so it is also an associated prime of $M$.
Some power of $\mfa$ annihilates $m$, and primality gives $\mfa\subseteq\mathfrak p$.
This proves the first equivalence, including $M=0$ with empty associated-prime set.

The [associated-prime finiteness theorem](https://stacks.math.columbia.edu/tag/00LC) and the [zero-divisor description](https://stacks.math.columbia.edu/tag/00LD) say that the zero divisors on a finite $M$ form the union of its finitely many associated primes.
Prime avoidance therefore supplies $x\in\mfa$ outside that union when none of those primes contains $\mfa$.
It acts injectively on $M$.
If $\mfa M\ne M$, the quotient $M/xM$ maps onto the nonzero module $M/\mfa M$, so $M/xM\ne0$.
Thus $x$ is an $M$-regular element under the proper-quotient convention.
Conversely, such an element implies $T^0(M)=0$ by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

If $M$ is finite and $\mfa M=M$, then $T^i(M)=0$ for every $i\ge0$.

::: pf-proof

For $M=0$, every derived functor is zero.
Otherwise choose generators $m_1,\ldots,m_s$ of $M$ and coefficients $c_{ij}\in\mfa$ with $m_i=\sum_j c_{ij}m_j$.
The adjugate identity for the matrix $1-(c_{ij})$ shows that its determinant annihilates each generator.
This determinant has the form $1-t$ with $t\in\mfa$.
Thus multiplication by $t$ on $M$ is the identity.

The endomorphism induced by multiplication by $t$ on $T^i(M)$ is also multiplication by $t$: multiply every term of an injective resolution by $t$ to obtain a chain map lifting the original scalar endomorphism.
Because the original map is the identity, functoriality makes this induced endomorphism the identity.
For any $z\in T^i(M)$, however, some $\mfa^q$ kills $z$, so $t^qz=0$.
Since $t$ acts identically, this implies $z=0$.
This proves every vanishing in the exceptional case, consistently with $\depth_\mfa M=\infty$.
Together with steps [](#s1){.pf-ref} and [](#s2){.pf-ref} it also completes (a).

:::

:::

::: {.pf-step #s4}

For finite $M$ with $\mfa M\ne M$, a regular sequence of length $n$ in $\mfa$ implies $T^i(M)=0$ for $i<n$.

::: pf-proof

Induct on $n$.
For $n=0$ there is nothing to prove; the case $n=1$ is step [](#s1){.pf-ref}.
Let $n>1$ and write $x$ for the first entry of a regular sequence of length $n$.
Put $N=M/xM$.
It is finite and $N/\mfa N\cong M/\mfa M\ne0$.
The other entries form an $N$-regular sequence of length $n-1$, so induction gives $T^j(N)=0$ for $j<n-1$.

Apply the derived-functor long exact sequence to
$$
0\longrightarrow M\xrightarrow{x}M\longrightarrow N\longrightarrow0.
$$
For $1\le i<n$, its segment
$$
T^{i-1}(N)\longrightarrow T^i(M)\xrightarrow{x}T^i(M)
$$
makes multiplication by $x$ injective, since the left term is zero.
But every element of $T^i(M)$ is killed by a power of $x$, by the ideal-torsion property.
Injectivity then forces $T^i(M)=0$.
Step [](#s1){.pf-ref} gives the missing degree zero, proving the induction.
The multiplication maps here are scalar multiplication by the chain-map argument in step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

For finite $M$ with $\mfa M\ne M$, vanishing of $T^i(M)$ for $i<n$ implies the existence of an $M$-regular sequence of length $n$ in $\mfa$.

::: pf-proof

Again induct on $n$.
For $n=0$ use the empty sequence; $M$ is nonzero because $\mfa M\ne M$.
For $n\ge1$, the hypothesis gives $T^0(M)=0$.
Step [](#s2){.pf-ref} supplies an $M$-regular element $x\in\mfa$.
Put $N=M/xM$; this is finite and $N/\mfa N\cong M/\mfa M\ne0$.

For $0\le j<n-1$, the long exact sequence from step [](#s4){.pf-ref} has a segment
$$
T^j(M)\longrightarrow T^j(N)\longrightarrow T^{j+1}(M)
$$
whose outer terms vanish.
Thus $T^j(N)=0$ for all $j<n-1$.
The induction hypothesis gives an $N$-regular sequence of length $n-1$ in $\mfa$.
Prepending $x$ gives an $M$-regular sequence of length $n$, with the same nonzero final quotient.
This proves the reverse induction without assuming a depth-drop formula.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove (a), with its arbitrary-module forward direction and its finite-module converse.
For $\mfa M\ne M$, steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (b) for every $n$.
For $\mfa M=M$, step [](#s3){.pf-ref} proves all the required vanishings and depth is infinite by convention.
Thus the equivalence in (b) holds for every finite module in the statement.

:::

:::

:::

::: {.remark title="The exceptional depth convention"}
The maximum-length definition without the exceptional convention is insufficient for arbitrary ideals.
For $A=k$, $\mfa=A$ and $M=k$, the functor $\Gamma_{\mfa}$ is zero on every module and all its derived functors vanish.
But no nonzero scalar is an $M$-regular element with nonzero quotient, and zero does not act injectively on $M$.
Setting $\depth_\mfa M=\infty$ for finite $M$ with $\mfa M=M$ resolves this case; see the [definition of ideal depth](https://stacks.math.columbia.edu/tag/00LE).
For a nonzero finite module over a local ring and a proper ideal, Nakayama's lemma excludes this exceptional case.
:::
