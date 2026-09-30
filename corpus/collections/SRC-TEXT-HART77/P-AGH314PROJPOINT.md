---
schema: qual/card@1
id: P-AGH314PROJPOINT
kind: problem
title: Projection from a point, and the cuspidal cubic image of the twisted cubic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Twisted Cubic
  - Cuspidal Cubic
relations:
- kind: uses
  target: P-AGH212DUPLE
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts, the center P, the hyperplane z=0, and the twisted-cubic parametrization with Hartshorne I.3.14. After a linear coordinate change, projection is deletion of the coordinate of the center; for the specified twisted cubic its plane image has equation y^3=x^2w.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the projective-coordinate morphism, image equality, and cusp calculation against two independent published solutions.'
---

::: {.problem}
Let $\PP^n$ be a hyperplane in $\PP^{n+1}$ and let $P \in \PP^{n+1} \sm \PP^n$.
Define $\phi: \PP^{n+1} \sm \theset{P} \to \PP^n$ by letting $\phi(Q)$ be the intersection with $\PP^n$ of the unique line through $P$ and $Q$.

(a) Show that $\phi$ is a morphism.

(b) Let $Y \subseteq \PP^3$ be the twisted cubic curve, the image of the $3$-uple embedding of $\PP^1$.
If $t, u$ are the homogeneous coordinates on $\PP^1$, then $Y$ is given parametrically by $(x,y,z,w) = (t^3, t^2 u, t u^2, u^3)$.
Let $P = \thevector{0 : 0 : 1 : 0}$ and let $\PP^2$ be the hyperplane $z = 0$.
Show that the projection of $Y$ from $P$ is a cuspidal cubic curve in the plane, and find its equation.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

After a projective linear change of coordinates, part (a) reduces to
$$
P=[0:\cdots:0:1],
\qquad
\PP^n=Z(x_{n+1})\subseteq\PP^{n+1}.
$$

::: pf-proof

Choose a nonzero vector representing $P$ and a basis of the vector hyperplane whose projectivization is the given $\PP^n$.
Since $P$ does not lie in that hyperplane, adjoining the representative of $P$ gives a basis of the ambient vector space.
The resulting linear automorphism of the vector space induces a projective automorphism carrying the pair $(P,\PP^n)$ to the displayed coordinate pair.
Conjugating the projection by projective automorphisms preserves the property of being a morphism.

:::

:::

::: {.pf-step #s2}

In these coordinates,
$$
\phi([a_0:\cdots:a_n:a_{n+1}])=[a_0:\cdots:a_n].
$$
This is a morphism on $\PP^{n+1}\setminus\{P\}$, proving (a).

::: pf-proof

For $Q=[a_0:\cdots:a_{n+1}]\ne P$, not all of $a_0,\ldots,a_n$ vanish.
The line through $P$ and $Q$ consists of the projective points represented by
$$
\lambda(a_0,\ldots,a_n,a_{n+1})+\mu(0,\ldots,0,1).
$$
Choosing $\mu=-\lambda a_{n+1}$ gives its unique intersection with $x_{n+1}=0$, namely
$$
[a_0:\cdots:a_n:0].
$$
After identifying that hyperplane with $\PP^n$, this is the displayed formula.

The coordinate functions $x_0,\ldots,x_n$ are homogeneous of the same degree and have no common zero on the domain $\PP^{n+1}\setminus\{P\}$.
Hence they define a morphism there [@Har10a, Chapter I, §3].

:::

:::

::: {.pf-step #s3}

For the data in part (b), projection from $P=[0:0:1:0]$ onto $z=0$ restricts to
$$
[t:u]\longmapsto[t^3:t^2u:u^3]
$$
in the plane coordinates $[x:y:w]$.

::: pf-proof

Here the coordinate of the center is $z$.
The same calculation as in step [](#s2){.pf-ref} therefore deletes the $z$-coordinate:
$$
[x:y:z:w]\longmapsto[x:y:w].
$$
Substituting the twisted-cubic parametrization
$$
[x:y:z:w]=[t^3:t^2u:tu^2:u^3]
$$
gives the displayed parametrization.
The center $P$ is not on $Y$, so this restriction is defined everywhere on $Y$.

:::

:::

::: {.pf-step #s4}

The image in $\PP^2$ is exactly the cubic
$$
C=Z(y^3-x^2w).
$$

::: pf-proof

Every parameterized point satisfies
$$
(t^2u)^3=(t^3)^2u^3,
$$
so the image is contained in $C$.

Conversely, let $[x:y:w]\in C$.
If $x\ne0$, normalize to $x=1$.
The equation becomes $w=y^3$, and the point is
$$
[1:y:y^3],
$$
which is the image of $[1:y]$.
If $x=0$, then $y^3=0$, so $y=0$ and the point is $[0:0:1]$, the image of $[0:1]$.
Thus every point of $C$ occurs.

:::

:::

::: {.pf-step #s5}

The cubic $C$ is cuspidal at $[0:0:1]$.

::: pf-proof

On the affine chart $w=1$ around $[0:0:1]$, its equation is
$$
y^3=x^2,
$$
with parametrization
$$
x=t^3,
\qquad
y=t^2.
$$
The origin is singular: for $F=y^3-x^2$, both partial derivatives vanish there in every characteristic.
It is the only singular point of the projective cubic $y^3-x^2w=0$: the equations
$$
F=0,
\qquad
F_x=-2xw=0,
\qquad
F_y=3y^2=0,
\qquad
F_w=-x^2=0
$$
force $x=y=0$, also in characteristics $2$ and $3$.
The lowest-degree term of the affine equation at the origin is $-x^2$, so the tangent cone is the doubled line $x=0$; together with the one-parameter normalization $t\mapsto(t^3,t^2)$, this is the standard cuspidal cubic.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove (a), and steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (b), with plane equation
$$
\boxed{y^3=x^2w}.
$$

:::

:::

:::
