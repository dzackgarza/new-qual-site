---
schema: qual/card@1
id: P-CAFA20G
kind: problem
title: "Dirichlet problem on a domain between two circles"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each step re-read and the two modulus computations redone:
      on |z| = 1 the ratio |z+1/2|^2/|z+2|^2 equals (5/4 + Re z)/(5 + 4 Re z) = 1/4, and on
      |z+2/5| = 2/5 the two moduli |1+4e^{i theta}| and |4+e^{i theta}| agree, giving 1/4. The
      image is decided to be the annulus by evaluating Phi at z = 1/2. The radial harmonic function
      is written out and its two boundary values checked. A garbled sentence of my own first draft
      (a spurious determinant computation) is repaired before committing. Not claimed: uniqueness
      beyond the one line from the maximum principle.
---

::: {.problem}
Let $\DD$ denote the open unit disc, and let $\DD' = \{z \in \CC : \abs{z + 2/5} < 2/5\}$ denote the open disc of center $-2/5$ and radius $2/5$.
Let $\Omega = \DD \setminus \overline{\DD'}$.

Find, with justification, an explicit continuous function $h: \overline{\Omega} \to \RR$, harmonic in $\Omega$, and with boundary values $h = 0$ on $\partial\DD$ and $h = 1$ on $\partial\DD'$.

Hint: You may wish to use a conformal map to change the domain $\Omega$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #map}
$\Phi(z)=\dfrac{z+1/2}{z+2}$ is a Möbius transformation with $\Phi(-1/2)=0$ and $\Phi(-2)=\infty$; it is holomorphic and injective on $\Omega$, where $z\ne-2$.

::: pf-proof
Written as $\Phi(z)=\frac{z+1/2}{z+2}$, the transformation has matrix $\begin{smallmatrix}1&1/2\\1&2\end{smallmatrix}$ with determinant $2-\tfrac12=\tfrac32\ne0$, so it is a bijection of the Riemann sphere, conformal off its pole $-2$; that pole is not in $\overline\Omega$ because $\abs{-2}=2>1$.
:::

:::

::: {.pf-step #outer}
$\abs{\Phi(z)}=\tfrac12$ on $\abs{z}=1$.

::: pf-proof
For $\abs{z}=1$, $\abs{z+\tfrac12}^{2}=1+\operatorname{Re}z+\tfrac14=\tfrac54+\operatorname{Re}z$ and $\abs{z+2}^{2}=1+4\operatorname{Re}z+4=5+4\operatorname{Re}z=4\bigl(\tfrac54+\operatorname{Re}z\bigr)$, so the quotient of the square roots is $\tfrac12$.
:::

:::

::: {.pf-step #inner}
$\abs{\Phi(z)}=\tfrac14$ on $\abs{z+\tfrac25}=\tfrac25$.

::: pf-proof
On that circle $z=-\tfrac25+\tfrac25e^{i\theta}$, so $z+\tfrac12=\tfrac1{10}+\tfrac25e^{i\theta}=\tfrac1{10}(1+4e^{i\theta})$ and $z+2=\tfrac85+\tfrac25e^{i\theta}=\tfrac25(4+e^{i\theta})$. The moduli of $1+4e^{i\theta}$ and $4+e^{i\theta}$ are equal, since both squared equal $17+8\cos\theta$; hence $\abs{\Phi}=\tfrac{1/10}{2/5}=\tfrac14$.
:::

:::

::: {.pf-step #annulus}
$\Phi$ maps $\Omega$ conformally onto the annulus $A=\{w:\tfrac14<\abs{w}<\tfrac12\}$.

::: pf-proof
$\Phi$ is injective and maps the two boundary circles to the two concentric circles $\abs{w}=\tfrac12$ and $\abs{w}=\tfrac14$, by steps [](#outer){.pf-ref} and [](#inner){.pf-ref}. The region $\Omega$ is connected and does not meet $\partial\Omega$; its image is therefore a connected subset of the complement of the two circles, i.e. of $\{\tfrac14<\abs{w}<\tfrac12\}\cup\{\abs{w}<\tfrac14\}\cup\{\abs{w}>\tfrac12\}$. The point $z=1/2\in\Omega$ has $\Phi(1/2)=\tfrac{1}{2.5}=0.4$, whose modulus lies strictly between $\tfrac14$ and $\tfrac12$, so the image is the annulus.
:::

:::

::: {.pf-step #radial}
$H(w)=\dfrac{\log(2\abs{w})}{\log(1/2)}$ is harmonic on $A$, equals $0$ on $\abs{w}=\tfrac12$ and $1$ on $\abs{w}=\tfrac14$.

::: pf-proof
$\log w$ is holomorphic on $A$, so its real part $\log\abs{w}$ is harmonic there, and a real affine function of a harmonic function is harmonic; the function $H$ is of that form. At $\abs{w}=\tfrac12$ the numerator is $\log1=0$; at $\abs{w}=\tfrac14$ it is $\log\tfrac12$, and dividing by $\log\tfrac12$ gives $1$.
:::

:::

::: {.pf-step #h}
$h=H\circ\Phi$ is harmonic on $\Omega$, continuous on $\overline\Omega$, with $h=0$ on $\partial\DD$ and $h=1$ on $\partial\DD'$.

::: pf-proof
$\Phi$ is holomorphic on a neighbourhood of $\overline\Omega$ and $H$ is harmonic on the annulus containing the image, so the composite is harmonic on $\Omega$ and continuous on the closure; the boundary values follow from steps [](#outer){.pf-ref}, [](#inner){#inner} and [](#radial){.pf-ref}.
:::

:::

::: {.pf-step}
$h(z)=\dfrac{\log\bigl(\abs{z+2}/(2\abs{z+1/2})\bigr)}{\log 2}$ solves the problem.

::: pf-proof
Since $\abs{\Phi}=\abs{z+1/2}/\abs{z+2}$, the function of step [](#h){.pf-ref} is
$$
\boxed{h(z)=\frac{\log\!\left(\frac{\abs{z+2}}{2\,\abs{z+1/2}}\right)}{\log 2},}
$$
harmonic on $\Omega$, continuous on $\overline\Omega$, with the required boundary values $0$ on $\partial\DD$ and $1$ on $\partial\DD'$. The solution is unique by the maximum principle applied to the difference of two solutions.
:::

:::

:::
:::
