---
schema: qual/card@1
id: P-AGH241FINPROPER
kind: problem
title: Finite morphisms are proper
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Morphisms
  - Finite Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.4.1 statement and the definitions of finite and proper morphisms.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Show that a finite morphism is proper.
:::

::: {.solution}
Let
\[
f:X\longrightarrow Y
\]
be finite.  We verify the three defining properties of a proper morphism.

::: pf

::: {.pf-step #s1}

The morphism $f$ is of finite type.

::: pf-proof

Let
\[
V=\Spec B\subseteq Y
\]
be affine.  Since $f$ is finite,
\[
f^{-1}(V)=\Spec A
\]
with $A$ finite as a $B$-module.

If $a_1,\ldots,a_n$ generate $A$ as a $B$-module, then they also generate $A$ as a $B$-algebra:
\[
A=B[a_1,\ldots,a_n],
\]
because the right side is a $B$-subalgebra containing the module generators and hence all of $A$.

Thus the affine criterion of Hartshorne II.3.3 shows that $f$ is of finite type.

:::

:::

::: {.pf-step #s2}

The morphism $f$ is separated.

::: pf-proof

Separatedness is local on the target, so work over
\[
V=\Spec B\subseteq Y,
\qquad
f^{-1}(V)=\Spec A.
\]
Then
\[
X\times_YX
\]
restricted over $V$ is
\[
\Spec(A\otimes_BA).
\]
The diagonal
\[
\Delta_f:X\longrightarrow X\times_YX
\]
is induced by the multiplication homomorphism
\[
\mu:A\otimes_BA\longrightarrow A,
\qquad
a\otimes a'\longmapsto aa'.
\]
This homomorphism is surjective because
\[
a=\mu(a\otimes1).
\]
A surjective ring homomorphism induces a closed immersion of spectra.  Hence the diagonal is a closed immersion affine-locally on $Y$, and therefore globally.  Thus $f$ is separated.

:::

:::

::: {.pf-step #s3}

Every base change of $f$ is finite.

::: pf-proof

Let
\[
Y'\longrightarrow Y
\]
be any morphism and put
\[
X'=X\times_YY'.
\]
This can be checked affine-locally.  If
\[
Y=\Spec B,
\qquad
X=\Spec A,
\qquad
Y'=\Spec B',
\]
with $A$ finite over $B$, then
\[
X'=\Spec(A\otimes_BB').
\]
If $a_1,\ldots,a_n$ generate $A$ as a $B$-module, then
\[
a_1\otimes1,\ldots,a_n\otimes1
\]
generate $A\otimes_BB'$ as a $B'$-module.  Hence the base-changed morphism is finite.

:::

:::

::: {.pf-step #s4}

Every base change of $f$ is a closed map.

::: pf-proof

By step [](#s3){.pf-ref} every base change is finite.  Hartshorne II.3.5(b) proves that finite morphisms are closed.  Hence every base change of $f$ is closed.

:::

:::

::: {.pf-step #s5}

Thus $f$ is universally closed.

::: pf-proof

Universal closedness means exactly that every base change of $f$ is a closed map.  This is step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Therefore
\[
\boxed{f\text{ is proper}.}
\]

::: pf-proof

By definition, a morphism is proper if it is separated, of finite type, and universally closed.  These three properties are steps [](#s2){.pf-ref}, [](#s1){.pf-ref} and [](#s5){.pf-ref}, respectively.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the required conclusion.

:::

:::

:::
