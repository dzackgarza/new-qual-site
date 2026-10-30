---
schema: qual/card@1
id: P-TIE-F09-11
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 11.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the OCR misreading of |z| = 1? as |z| = 12 and labelled the parts (a)-(c), matching the source reference to (a), against Fall 2009, question 11, page 3 of Questions_from_Tie.pdf (read from the page image).
---

::: {.problem}
Let $g$ be analytic for $\abs{z} \le 1$ and $\abs{g(z)} < 1$ for $\abs{z} = 1$.

(a) Show that $g$ has a unique fixed point in $\abs{z} < 1$.

(b) What happens if we replace $\abs{g(z)} < 1$ with $\abs{g(z)} \le 1$ for $\abs{z} = 1$? Give an example if (a) is not true or give an proof if (a) is still true.

(c) What happens if we simply assume that $f$ is analytic for $\abs{z} < 1$ and $\abs{f(z)} < 1$ for $\abs{z} < 1$? Suppose that $f(z) \not\equiv z$. Can $f$ have more than one fixed point in $\abs{z} < 1$?

Hint: The map $\psi_\alpha(z) = \frac{\alpha - z}{1 - \bar{\alpha} z}$ may be useful.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Under the hypotheses of part (a), the function
$$
h(z)=z-g(z)
$$
has exactly one zero in $\abs{z}<1$, counted with multiplicity.


::: pf-proof

On $\abs{z}=1$,
$$
\abs{g(z)}<1=\abs{z}.
$$
Thus
$$
\abs{h(z)-z}=\abs{g(z)}<\abs{z}.
$$
By Rouché's theorem, $h$ and $z$ have the same number of zeros in the unit disk, counted with
multiplicity. The function $z$ has exactly one zero there, with multiplicity one. Hence so does
$h$.

:::

:::

::: {.pf-step #s1-2}

Therefore $g$ has a unique fixed point in $\abs{z}<1$.


::: pf-proof

The fixed points of $g$ are precisely the zeros of
$$
h(z)=z-g(z).
$$
Step [](#s1-1){.pf-ref} gives exactly one such zero in the disk.

:::

:::

::: {.pf-step #s1-3}

The conclusion of part (a) is false if the boundary hypothesis is weakened to
$$
\abs{g(z)}\le1
\qquad
\text{for }\abs{z}=1.
$$


::: pf-proof

Take
$$
g(z)=z.
$$
Then $g$ is analytic on the closed disk and satisfies
$$
\abs{g(z)}=1
$$
on the unit circle, but every point of the unit disk is a fixed point. Thus uniqueness fails.

:::

:::

::: {.pf-step #s1-4}

For $\alpha\in\DD$, the map
$$
\psi_\alpha(z)=\frac{\alpha-z}{1-\bar\alpha z}
$$
is an automorphism of the unit disk satisfying
$$
\psi_\alpha(\alpha)=0,
\qquad
\psi_\alpha(0)=\alpha,
\qquad
\psi_\alpha^{-1}=\psi_\alpha.
$$


::: pf-proof

Direct substitution gives the first two identities and
$$
\psi_\alpha(\psi_\alpha(z))=z.
$$
Moreover,
$$
1-\abs{\psi_\alpha(z)}^2
=
\frac{(1-\abs{\alpha}^2)(1-\abs{z}^2)}
{\abs{1-\bar\alpha z}^2}.
$$
Hence $\abs{z}<1$ if and only if $\abs{\psi_\alpha(z)}<1$, so $\psi_\alpha$ is a biholomorphic
self-map of the disk.

:::

:::

::: {.pf-step #s1-5}

Suppose the map $f$ in part (c) has a fixed point $\alpha\in\DD$. Then
$$
H=\psi_\alpha\circ f\circ\psi_\alpha
$$
is an analytic self-map of $\DD$ with $H(0)=0$.


::: pf-proof

Step [](#s1-4){.pf-ref} shows that both occurrences of $\psi_\alpha$ map $\DD$ biholomorphically onto itself,
while the hypothesis of part (c) gives $f(\DD)\subseteq\DD$. Thus $H$ is an analytic self-map.
Since $\psi_\alpha(0)=\alpha$ and $f(\alpha)=\alpha$,
$$
H(0)
=
\psi_\alpha(f(\alpha))
=
\psi_\alpha(\alpha)
=0.
$$

:::

:::

::: {.pf-step #s1-6}

If $H:\DD\to\DD$ is analytic, $H(0)=0$, and $H(\gamma)=\gamma$ for some
$0\ne\gamma\in\DD$, then
$$
H(z)=z
$$
for all $z\in\DD$.


::: pf-proof

Schwarz's lemma gives
$$
\abs{H(z)}\le\abs{z}
$$
for every $z\in\DD$. At the nonzero fixed point $\gamma$,
$$
\abs{H(\gamma)}=\abs{\gamma},
$$
so equality occurs at a nonzero point. The equality case of Schwarz's lemma therefore gives
$$
H(z)=\lambda z
$$
for some $\abs{\lambda}=1$. Since $H(\gamma)=\gamma$ and $\gamma\ne0$, one has $\lambda=1$.

:::

:::

::: {.pf-step #s1-7}

If $f:\DD\to\DD$ is analytic and $f\not\equiv\operatorname{id}_{\DD}$, then $f$ has
at most one fixed point in $\DD$.


::: pf-proof

Suppose $f$ had distinct fixed points $\alpha,\beta\in\DD$. Define $H$ as in step [](#s1-5){.pf-ref} and put
$$
\gamma=\psi_\alpha(\beta).
$$
Because $\beta\ne\alpha$, step [](#s1-4){.pf-ref} gives $\gamma\ne0$. Also
$$
\begin{aligned}
H(\gamma)
&=
\psi_\alpha\!\left(
f(\psi_\alpha(\gamma))
\right)\\
&=
\psi_\alpha(f(\beta))
=
\psi_\alpha(\beta)
=
\gamma.
\end{aligned}
$$
By step [](#s1-6){.pf-ref}, $H$ is the identity. Conjugating by $\psi_\alpha$ then gives
$$
f=\operatorname{id}_{\DD},
$$
contrary to the hypothesis. Hence two distinct fixed points are impossible.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), step [](#s1-3){.pf-ref} answers part (b), and step [](#s1-7){.pf-ref} answers part (c).

:::

:::

:::
