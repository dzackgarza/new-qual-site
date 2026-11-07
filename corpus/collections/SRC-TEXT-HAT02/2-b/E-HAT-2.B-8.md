---
schema: qual/card@1
id: E-HAT-2.B-8
kind: problem
title: "Real division algebras and the Borsuk--Ulam theorem"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the determinant or transfer-sequence argument, including the mod-2 endpoint maps.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 8, printed page
    177; the statement matches word for word. Checked: in a division algebra left
    multiplication L_a is bijective for a ≠ 0, so det L_a ≠ 0; a path in
    R^{2n+1} − {0} joins a to −a, and det L_{−a} = (−1)^{2n+1} det L_a = −det L_a, so
    t ↦ det L_{γ(t)} is a path in R − {0} from d to −d, which is impossible. This
    gives the theorem for the odd dimensions 3, 5, 7 in place of the division-algebra
    classification (Theorem 2B.5, p. 173). No defect.
---
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Directly read DeMason, M382C Full Credit HW Problems (2021), Hatcher 2.B.8, printed p.71. Both
    use a path from a to -a avoiding the origin. A division algebra makes L_a an isomorphism
    because ax=b is solvable for every b, and the dimension being odd makes det L_{-a}=-det L_a;
    continuity forces a zero determinant between endpoints, exactly contradicting step s1. No
    additional claim is imported from the source's optional degree-of-maps remark.

---

::: {.problem}
Show that $\RR^{2n+1}$ is not a division algebra over $\RR$ if $n > 0$ by considering how the determinant of the linear map $x \mapsto ax$ given by the multiplication in a division algebra structure would vary as $a$ moves along a path in $\RR^{2n+1} - \{0\}$ joining two antipodal points.
:::

::: {.solution}
Assume for contradiction that $A=\RR^{2n+1}$, with $n>0$, has the structure of a real division algebra. For $a\in A$ let
$$
L_a:A\to A,\qquad L_a(x)=ax.
$$

::: pf

::: {.pf-step #s1}

If $a\ne0$, then $L_a$ is invertible, hence
$$
\det L_a\ne0.
$$

::: pf-proof

In a division algebra the equation $ax=b$ is solvable for every $b$ whenever $a\ne0$, so $L_a$ is surjective. Since $A$ is finite-dimensional, $L_a$ is therefore an isomorphism.

:::

:::

::: pf-step

Choose $a\ne0$. Since $2n+1\ge3$, there is a path
$$
\gamma:[0,1]\to A-\{0\}
$$
with $\gamma(0)=a$ and $\gamma(1)=-a$.

::: pf-proof

The punctured Euclidean space $\RR^{2n+1}-\{0\}$ is path-connected when $2n+1>1$; for instance join antipodal points by a semicircle on the sphere of radius $\norm{a}$.

:::

:::

::: {.pf-step #s3}

The function
$$
t\longmapsto \det L_{\gamma(t)}
$$
is continuous and never zero, but its endpoint values have opposite signs.

::: pf-proof

Bilinearity of multiplication implies that the matrix entries of $L_a$ depend linearly, hence continuously, on $a$. Thus the determinant depends continuously on $a$. By step [](#s1){.pf-ref} it never vanishes along $\gamma$. On the other hand
$$
L_{-a}=-L_a,
$$
so, because the dimension $2n+1$ is odd,
$$
\det L_{-a}=(-1)^{2n+1}\det L_a=-\det L_a.
$$

:::

:::

::: pf-step

This is impossible.

::: pf-proof

A continuous nonzero real-valued function on the connected interval $[0,1]$ has constant sign. The endpoint calculation in step [](#s3){.pf-ref} contradicts this.

:::

:::

:::

Hence
$$
\boxed{\RR^{2n+1}\text{ admits no real division-algebra structure for }n>0.}
$$The continuous determinant path is printed in **Kenneth DeMason, *M382C Full Credit HW Problems* (2021)**, Hatcher 2.B.8, printed p. 71 of the local PDF `tmp/sources/demason-m382c-hatcher-20210404.pdf`. As in the source, step [](#s1){.pf-ref} makes every left multiplication by a nonzero element invertible by solvability of $ax=b$, step [](#s3){.pf-ref} gives the sign change $\det L_{-a}=-\det L_a$ in odd dimension, and step [](#s4){.pf-ref} obtains the contradiction in closed form. The optional degree-of-maps remark in the source is not needed and is not used here.


:::
