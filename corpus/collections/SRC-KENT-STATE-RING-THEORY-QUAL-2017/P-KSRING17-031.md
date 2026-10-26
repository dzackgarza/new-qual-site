---
schema: qual/card@1
id: P-KSRING17-031
kind: problem
title: A non-surjective injective endomorphism of a field
classification:
  areas: [algebra]
  topics: []
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

::: pf-step

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

::: pf-step

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

::: pf-step

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

::: pf-step

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

::: pf-step

The element
$$
t\in F
$$
does not lie in $\operatorname{im}\varphi$.


::: pf-proof

By step <1>3,
$$
\operatorname{im}\varphi
\subseteq
\QQ(t^2).
$$
By step <1>4, every element of the image is fixed by $\sigma$.
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

::: pf-step

Therefore $\varphi$ is not surjective.


::: pf-proof

Step <1>5 exhibits an element of $F$ with no preimage.

:::

:::

::: pf-step

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

Steps <1>1--<1>2 show that $\varphi$ is an injective ring homomorphism, while step <1>6 shows that it is not onto.

:::

:::

::: pf-qed

Step <1>7 verifies the requested example.

:::

:::
