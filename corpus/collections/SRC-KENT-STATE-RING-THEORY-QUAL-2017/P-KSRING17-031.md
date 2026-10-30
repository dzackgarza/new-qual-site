---
schema: qual/card@1
id: P-KSRING17-031
kind: problem
title: A non-surjective injective endomorphism of a field
classification:
  areas: [algebra]
  topics:
  - Field Homomorphisms
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 31 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow in the map and set the statement in LaTeX against problem 31 on Ring_Theory_Qual_Problems.pdf PDF page 7.
---

::: {.problem}
Give an example of a field $F$ and a one-to-one ring homomorphism $\varphi : F \to F$ which is not onto.
Verify your example.
:::

::: {.solution}

Take
$$
\boxed{
F=\QQ(t),
}
$$
the rational function field in one indeterminate over $\QQ$, and define
$$
\boxed{
\varphi:F\to F,
\qquad
\varphi(f(t))
\coloneqq
f(t^2).
}
$$

::: pf

::: {.pf-step #s1-1}

The map $\varphi$ is a well-defined ring homomorphism.


::: pf-proof

An element of $\QQ(t)$ has the form
$$
\frac{p(t)}{q(t)}
$$
with
$$
p,q\in\QQ[t],
\qquad
q\ne0.
$$
Define
$$
\varphi\left(\frac{p(t)}{q(t)}\right)
\coloneqq
\frac{p(t^2)}{q(t^2)}.
$$
Since $t^2$ is transcendental over $\QQ$, a nonzero polynomial $q$ cannot satisfy
$$
q(t^2)=0.
$$
Thus the denominator remains nonzero.

The substitution
$$
t\longmapsto t^2
$$
preserves addition, multiplication, and $1$, so $\varphi$ is a unital ring homomorphism.

:::

:::

::: {.pf-step #s1-2}

The map $\varphi$ is injective.


::: pf-proof

Suppose
$$
\varphi\left(\frac{p(t)}{q(t)}\right)=0.
$$
Then
$$
p(t^2)=0.
$$
Because $t^2$ is transcendental over $\QQ$, this implies
$$
p=0.
$$
Hence
$$
\frac{p(t)}{q(t)}=0.
$$
Therefore
$$
\ker\varphi=0,
$$
so $\varphi$ is injective.

:::

:::

::: {.pf-step #s1-3}

The image of $\varphi$ is contained in
$$
\QQ(t^2).
$$


::: pf-proof

Every image element has the form
$$
f(t^2)
$$
with
$$
f\in\QQ(t).
$$
Such an element is, by definition, a rational function in $t^2$. Hence
$$
\operatorname{im}\varphi
\subseteq
\QQ(t^2).
$$

:::

:::

::: {.pf-step #s1-4}

Every element of
$$
\QQ(t^2)
$$
is fixed by the field automorphism
$$
\sigma:\QQ(t)\to\QQ(t),
\qquad
\sigma(t)=-t.
$$


::: pf-proof

If
$$
g\in\QQ(t^2),
$$
then
$$
g=h(t^2)
$$
for some
$$
h\in\QQ(t).
$$
Therefore
$$
\sigma(g)
=
h((-t)^2)
=
h(t^2)
=
g.
$$

:::

:::

::: {.pf-step #s1-5}

The element
$$
t\in F
$$
does not lie in $\operatorname{im}\varphi$.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\operatorname{im}\varphi
\subseteq
\QQ(t^2).
$$
By step [](#s1-4){.pf-ref}, every element of the image is fixed by $\sigma$.
But
$$
\sigma(t)
=
-t
\ne
t.
$$
Thus
$$
t\notin\operatorname{im}\varphi.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore $\varphi$ is not surjective.


::: pf-proof

Step [](#s1-5){.pf-ref} exhibits an element of $F$ with no preimage.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
F=\QQ(t),
\qquad
\varphi(f(t))=f(t^2)
}
$$
is the required example.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} show that $\varphi$ is an injective ring homomorphism, while step [](#s1-6){.pf-ref} shows that it is not onto.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} verifies the requested example.

:::

:::

:::
