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
<1>1. Under the hypotheses of part (a), the function
$$
h(z)=z-g(z)
$$
has exactly one zero in $\abs{z}<1$, counted with multiplicity.

::: {.proof}
On $\abs{z}=1$,
$$
|g(z)|<1=|z|.
$$
Thus
$$
|h(z)-z|=|g(z)|<|z|.
$$
By Rouché's theorem, $h$ and $z$ have the same number of zeros in the unit disk, counted with
multiplicity. The function $z$ has exactly one zero there, with multiplicity one. Hence so does
$h$.
:::

<1>2. Therefore $g$ has a unique fixed point in $\abs{z}<1$.

::: {.proof}
The fixed points of $g$ are precisely the zeros of
$$
h(z)=z-g(z).
$$
Step <1>1 gives exactly one such zero in the disk.
:::

<1>3. The conclusion of part (a) is false if the boundary hypothesis is weakened to
$$
|g(z)|\le1
\qquad
\text{for }|z|=1.
$$

::: {.proof}
Take
$$
g(z)=z.
$$
Then $g$ is analytic on the closed disk and satisfies
$$
|g(z)|=1
$$
on the unit circle, but every point of the unit disk is a fixed point. Thus uniqueness fails.
:::

<1>4. For $\alpha\in\DD$, the map
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

::: {.proof}
Direct substitution gives the first two identities and
$$
\psi_\alpha(\psi_\alpha(z))=z.
$$
Moreover,
$$
1-|\psi_\alpha(z)|^2
=
\frac{(1-|\alpha|^2)(1-|z|^2)}
{|1-\bar\alpha z|^2}.
$$
Hence $|z|<1$ if and only if $|\psi_\alpha(z)|<1$, so $\psi_\alpha$ is a biholomorphic
self-map of the disk.
:::

<1>5. Suppose the map $f$ in part (c) has a fixed point $\alpha\in\DD$. Then
$$
H=\psi_\alpha\circ f\circ\psi_\alpha
$$
is an analytic self-map of $\DD$ with $H(0)=0$.

::: {.proof}
Step <1>4 shows that both occurrences of $\psi_\alpha$ map $\DD$ biholomorphically onto itself,
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

<1>6. If $H:\DD\to\DD$ is analytic, $H(0)=0$, and $H(\gamma)=\gamma$ for some
$0\ne\gamma\in\DD$, then
$$
H(z)=z
$$
for all $z\in\DD$.

::: {.proof}
Schwarz's lemma gives
$$
|H(z)|\le|z|
$$
for every $z\in\DD$. At the nonzero fixed point $\gamma$,
$$
|H(\gamma)|=|\gamma|,
$$
so equality occurs at a nonzero point. The equality case of Schwarz's lemma therefore gives
$$
H(z)=\lambda z
$$
for some $|\lambda|=1$. Since $H(\gamma)=\gamma$ and $\gamma\ne0$, one has $\lambda=1$.
:::

<1>7. If $f:\DD\to\DD$ is analytic and $f\not\equiv\operatorname{id}_{\DD}$, then $f$ has
at most one fixed point in $\DD$.

::: {.proof}
Suppose $f$ had distinct fixed points $\alpha,\beta\in\DD$. Define $H$ as in step <1>5 and put
$$
\gamma=\psi_\alpha(\beta).
$$
Because $\beta\ne\alpha$, step <1>4 gives $\gamma\ne0$. Also
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
By step <1>6, $H$ is the identity. Conjugating by $\psi_\alpha$ then gives
$$
f=\operatorname{id}_{\DD},
$$
contrary to the hypothesis. Hence two distinct fixed points are impossible.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), step <1>3 answers part (b), and step <1>7 answers part (c).
:::
:::
