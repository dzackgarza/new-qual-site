---
schema: qual/card@1
id: P-TIE-F11-11
kind: problem
title: Fixed points of analytic self-maps of the disk
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 11.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the OCR misreading of |z| = 1? as |z| = 12 and labelled the bulleted parts (a)-(c), matching the source reference to (a), against Fall 2011, question 11, pages 5-6 of Questions_from_Tie.pdf.
---

::: {.problem}
Let $g$ be analytic for $\abs{z} \le 1$ and $\abs{g(z)} < 1$ for $\abs{z} = 1$.

(a) Show that $g$ has a unique fixed point in $\abs{z} < 1$.

(b) What happens if we replace $\abs{g(z)} < 1$ with $\abs{g(z)} \le 1$ for $\abs{z} = 1$? Give an example if (a) is not true or give an proof if (a) is still true.

(c) What happens if we simply assume that $f$ is analytic for $\abs{z} < 1$ and $\abs{f(z)} < 1$ for $\abs{z} < 1$? Suppose that $f(z) \not\equiv z$. Can $f$ have more than one fixed point in $\abs{z} < 1$?

Hint: The map $\psi_\alpha(z) = \frac{\alpha - z}{1 - \bar{\alpha} z}$ may be useful.
:::

::: {.solution}
<1>1. Under the hypotheses of part (a), $g$ has exactly one fixed point in $\abs{z}<1$.

::: {.proof}
A fixed point of $g$ is a zero of
$$
H(z)\coloneqq z-g(z).
$$
On $\abs{z}=1$,
$$
\abs{H(z)-z}
=
\abs{g(z)}
<1
=
\abs{z}.
$$
By Rouché's theorem, $H$ and $z$ have the same number of zeros in $\abs{z}<1$, counted with multiplicity. Since $z$ has exactly one zero there, $H$ has exactly one zero there. Thus $g$ has a unique fixed point in the open unit disk.
:::

<1>2. If the boundary hypothesis is weakened to $\abs{g(z)}\le1$ on $\abs{z}=1$, the conclusion of part (a) can fail.

::: {.proof}
Consider
$$
g(z)=\frac{z+1}{2}.
$$
This function is analytic on the closed unit disk, and for $\abs{z}=1$,
$$
\abs{g(z)}
=
\frac{\abs{z+1}}2
\le1.
$$
Its fixed-point equation is
$$
z=\frac{z+1}{2},
$$
whose unique solution is $z=1$. Hence $g$ has no fixed point in $\abs{z}<1$. Thus the strict boundary inequality in part (a) cannot be replaced by a non-strict one.

Moreover, uniqueness can also fail under the non-strict hypothesis: the identity map $g(z)=z$ satisfies $\abs{g(z)}=1$ on $\abs{z}=1$ and every point of the disk is fixed.
:::

<1>3. For $\alpha\in\DD$, the map
$$
\psi_\alpha(z)=\frac{\alpha-z}{1-\overline\alpha z}
$$
is an automorphism of $\DD$ satisfying $\psi_\alpha(\alpha)=0$ and $\psi_\alpha^{-1}=\psi_\alpha$.

::: {.proof}
The denominator does not vanish for $\abs{z}<1$, because
$$
\abs{\overline\alpha z}<1.
$$
A direct computation gives
$$
1-\abs{\psi_\alpha(z)}^2
=
\frac{(1-\abs{\alpha}^2)(1-\abs{z}^2)}
{\abs{1-\overline\alpha z}^2},
$$
which is positive for $\alpha,z\in\DD$. Hence $\psi_\alpha$ maps $\DD$ into itself. Direct substitution gives $\psi_\alpha(\alpha)=0$ and
$$
\psi_\alpha(\psi_\alpha(z))=z,
$$
so $\psi_\alpha$ is an automorphism and is its own inverse.
:::

<1>4. If $f:\DD\to\DD$ is analytic, $f\not\equiv\operatorname{id}$, and $\alpha\in\DD$ is a fixed point of $f$, then $f$ has no second fixed point in $\DD$.

::: {.proof}
Suppose, for contradiction, that $\beta\in\DD$ is another fixed point with $\beta\ne\alpha$. Define
$$
h
\coloneqq
\psi_\alpha\circ f\circ\psi_\alpha.
$$
By step <1>3, $h:\DD\to\DD$ is analytic. Since $f(\alpha)=\alpha$ and $\psi_\alpha(0)=\alpha$,
$$
h(0)=0.
$$
Set
$$
\gamma\coloneqq\psi_\alpha(\beta).
$$
Because $\beta\ne\alpha$, one has $\gamma\ne0$, and because $f(\beta)=\beta$,
$$
h(\gamma)=\gamma.
$$
Schwarz's lemma gives $\abs{h(z)}\le\abs{z}$ on $\DD$. Equality holds at the nonzero point $\gamma$, so the equality case of Schwarz's lemma implies
$$
h(z)=e^{it}z
$$
for some real $t$. Since $h(\gamma)=\gamma$ and $\gamma\ne0$, one has $e^{it}=1$, hence $h=\operatorname{id}$. Conjugating by $\psi_\alpha$ then gives $f=\operatorname{id}$, contradicting the hypothesis. Therefore no second fixed point exists.
:::

<1>5. Consequently, the answer to part (c) is
$$
\boxed{\text{$f$ cannot have more than one fixed point in $\abs{z}<1$ unless $f\equiv\operatorname{id}$.}}
$$

::: {.proof}
If $f$ has a fixed point, step <1>4 shows that it is unique unless $f$ is the identity. If $f$ has no fixed point, the assertion is immediate.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), step <1>2 proves part (b), and step <1>5 proves part (c).
:::
:::
