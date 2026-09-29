---
schema: qual/card@1
id: P-AGH277VERONESESURF
kind: problem
title: The Veronese surface and rational surfaces from linear systems
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Veronese Embedding
  - Ruled Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts with the retained Hartshorne II.7.7 transcription. Corrected the characteristic-two failure in part (b) by an explicit tangent vector, proved the remaining characteristic case on affine charts, and constructed the blowup embedding, its cubic hyperplane section, and its ruling in part (c). For an arbitrary ground field, the fixed point in part (c) is taken to be k-rational.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be a field, let $X = \PP^2_k$, and let $\abs{D}$ be the complete linear system of all divisors of degree $2$ on $X$, the conics.
Here $D$ corresponds to the invertible sheaf $\OO(2)$, whose space of global sections has basis $x^2, y^2, z^2, xy, xz, yz$, where $x, y, z$ are the homogeneous coordinates of $X$.

(a) The complete linear system $\abs{D}$ gives an embedding of $\PP^2$ in $\PP^5$, whose image is the **Veronese surface** (I, Ex. 2.13).

(b) Assume $\operatorname{char}k\ne2$.
Show that the subsystem defined by $x^2, y^2, z^2, y(x - z), (x - y)z$ gives a closed immersion of $X$ into $\PP^4$.
   The image is called the Veronese surface in $\PP^4$. Cf. (IV, Ex. 3.11).
In characteristic two, show instead that this specified map is not an immersion.

(c) Let $\nu \subseteq \abs{D}$ be the linear system of all conics passing through a fixed $k$-rational point $P$.
   Then $\nu$ gives an immersion of $U = X - P$ into $\PP^4$.
   Furthermore, if we blow up $P$ to get a surface $\tilde X$, then this map extends to a closed immersion of $\tilde X$ in $\PP^4$.

   Show that $\tilde X$ is a surface of degree $3$ in $\PP^4$, and that the lines in $X$ through $P$ are transformed into straight lines in $\tilde X$ which do not meet.
   Since $\tilde X$ is the union of all these lines, we say $\tilde X$ is a **ruled surface** (V, 2.19.1).
Over an arbitrary field, this ruling means a $\PP^1$-bundle over $\PP_k^1$ whose geometric fibres are embedded as lines.
:::

::: {.solution}
The maps in parts (a) and (b) are defined everywhere because the sections $x^2,y^2,z^2$ have no common zero.
In part (c), choose projective coordinates with $P=[0:0:1]$; this is possible because $P$ is $k$-rational.

::: pf

::: {.pf-step #s1}
The complete conic system defines the closed immersion
$$
v_2:\PP_k^2\longrightarrow\PP_k^5,\qquad
[x:y:z]\longmapsto[x^2:y^2:z^2:xy:xz:yz].
$$

::: pf-proof
These six sections form the complete degree-two monomial basis, so the map is the second Veronese map [@Har10a, Exercises I.2.13 and I.3.4].
Its local embedding property is explicit: on the target chart where the coordinate $x^2$ is nonzero, the inverse image is $x\ne0$.
The coordinate functions $y/x$ and $z/x$ are the pullbacks of $xy/x^2$ and $xz/x^2$, so the map on coordinate rings is surjective.
The same argument on the $y^2$ and $z^2$ charts gives a closed immersion into their union, which contains the whole image.
The morphism is proper because its source is projective and its target is separated over $k$.
A proper immersion is a closed immersion, proving (a) in every characteristic.
:::

:::

::: {.pf-step #s2}
If $\operatorname{char}k\ne2$, the morphism
$$
f:\PP_k^2\longrightarrow\PP_k^4,\qquad
[x:y:z]\longmapsto[x^2:y^2:z^2:xy-yz:xz-yz]
$$
is a closed immersion.

::: pf-proof
Write target coordinates as $[a:b:c:d:e]$.
On $a\ne0$, use the same letters $b,c,d,e$ for their ratios to $a$.
The inverse image is $x\ne0$, with coordinates $u=y/x$ and $v=z/x$, and the map on coordinate rings is
$$
b\longmapsto u^2,\quad c\longmapsto v^2,\quad
d\longmapsto u-uv,\quad e\longmapsto v-uv.
$$
In particular, $d-e$ pulls back to $u-v$.
The opens $1+d-e\ne0$ and $1-d+e\ne0$ cover this target chart because their sum is the nonzero constant $2$.

On the first open, the inverse-image coordinate ring is $k[u,v,(1+u-v)^{-1}]$, and its generators are in the image because
$$
u=\frac{b+d}{1+d-e},\qquad v=u-(d-e).
$$
Here the identities follow from $u^2+u-uv=u(1+u-v)$.
The inverse of $1+u-v$ is also the image of an inverted target coordinate, so the localized ring map is surjective.
On the second open the same conclusion follows from
$$
v=\frac{c+e}{1-d+e},\qquad u=v+(d-e).
$$
Thus the map is a closed immersion over the chart $a\ne0$.

The cyclic change $(x,y,z)\mapsto(y,z,x)$ sends the five defining sections to
$$
(y^2,z^2,x^2,-(xz-yz),(xy-yz)-(xz-yz)).
$$
This is an invertible linear change of the five target coordinates.
It transfers the same affine-ring calculation to the charts $b\ne0$ and $c\ne0$.
These three target charts contain the image, so $f$ is an immersion there.
As in step [](#s1){.pf-ref}, properness makes it a closed immersion into $\PP^4$.
:::

:::

::: {.pf-step #s3}
In characteristic two, the map in step [](#s2){.pf-ref} is not an immersion.

::: pf-proof
Let $R=k[\varepsilon]/(\varepsilon^2)$.
The $R$-point $[1:1+\varepsilon:\varepsilon]$ is a nonconstant tangent vector at $[1:1:0]$.
In characteristic two its five coordinates under $f$ are
$$
1,\quad (1+\varepsilon)^2=1,\quad\varepsilon^2=0,
\quad(1+\varepsilon)(1-\varepsilon)=1,
\quad(1-(1+\varepsilon))\varepsilon=0.
$$
Thus its image is the constant $R$-point $[1:1:0:1:0]$, the same image as the constant vector at $[1:1:0]$.
An immersion is a monomorphism and cannot identify these two morphisms $\Spec R\to\PP^2$.
Equivalently, this is a nonzero vector in the kernel of the tangent map.
:::

:::

::: {.pf-step #s4}
The blowup at $P$ is the incidence surface
$$
B=\{([x:y:z],[s:t])\in\PP_k^2\times_k\PP_k^1:xt=ys\}.
$$
Its first projection $\pi:B\to\PP^2$ is an isomorphism away from $P$, and its exceptional curve is $E=\{P\}\times\PP^1$.

::: pf-proof
Away from $P$, the equation forces $[s:t]=[x:y]$, giving an inverse to the first projection.
On the affine chart $z=1$, the incidence equation gives exactly the [[D-SCHBLOWUP|Rees-algebra construction]] of the blowup of the ideal $(x,y)$.
It therefore agrees with the blowup over the open cover consisting of $z\ne0$ and $\PP^2\setminus\{P\}$, and the identifications agree on their overlap.
This proves the global description and the exceptional fibre.

On $s\ne0$, put $u=t/s$.
The equation becomes $y=ux$, giving coordinates $(u,[x:z])$ and an isomorphism with $\AA_k^1\times_k\PP_k^1$.
On $t\ne0$, put $v=s/t$ and obtain coordinates $(v,[y:z])$ with $x=vy$.
These charts show that $B$ is a smooth projective integral surface.
:::

:::

::: {.pf-step #s5}
The conics through $P$ give a morphism $j:B\to\PP^4$ extending the map from $U=\PP^2\setminus\{P\}$.

::: pf-proof
The conics vanishing at $P$ have basis $x^2,xy,y^2,xz,yz$.
Their common zero locus on $\PP^2$ is just $P$, so they define the required map on $U$.
On the two charts of step [](#s4){.pf-ref}, define
$$
\begin{aligned}
j_s(u,[x:z])&=[x:ux:u^2x:z:uz],\\
j_t(v,[y:z])&=[v^2y:vy:y:vz:z].
\end{aligned}
$$
Neither list has a common zero, since $[x:z]$ and $[y:z]$ are projective coordinates.
On the overlap, $v=u^{-1}$ and $y=ux$, and the first list is $u$ times the second.
Thus these formulas glue to a morphism $j$.
Where $x\ne0$, its first formula is the list $[x^2:xy:y^2:xz:yz]$ divided by $x$; the second formula has the analogous division by $y$.
Hence it extends the original map on $U$.
:::

:::

::: {.pf-step #s6}
The morphism $j$ is a closed immersion with image
$$
\Sigma=V_+(ac-b^2,\ ae-bd,\ be-cd)\subseteq\PP_k^4,
$$
where $[a:b:c:d:e]$ are the target coordinates in step [](#s5){.pf-ref}.

::: pf-proof
Substitution of either local formula in step [](#s5){.pf-ref} makes the three equations vanish, so $j$ factors through $\Sigma$ as a scheme.
The affine opens $a\ne0$, $c\ne0$, $d\ne0$, and $e\ne0$ cover $\Sigma$: if these four coordinates vanish at a point, $ac=b^2$ forces $b=0$ as well.

On $a\ne0$, set $a=1$.
The equations give $c=b^2$ and $e=bd$, with $b,d$ free; thus this chart is $\Spec k[b,d]$.
The map $j_s$ identifies it with the chart $s\ne0$, $x\ne0$ on $B$, by $b=u$ and $d=z/x$.
On $d\ne0$, set $d=1$.
The equations give $b=ae$ and $c=ae^2$, so this chart is $\Spec k[a,e]$ and $j_s$ identifies it with $s\ne0$, $z\ne0$, by $a=x/z$ and $e=u$.

On $c\ne0$, set $c=1$.
The equations give $a=b^2$ and $d=be$; the free coordinates $b,e$ correspond under $j_t$ to $v,z/y$.
On $e\ne0$, set $e=1$.
The equations give $b=cd$ and $a=cd^2$; the free coordinates $c,d$ correspond under $j_t$ to $y/z,v$.
Thus $j$ is an isomorphism over every member of an affine open cover of $\Sigma$, and hence $B\cong\Sigma$.
Since $\Sigma$ is a closed subscheme of $\PP^4$, $j$ is a closed immersion.
Its restriction to $B\setminus E\cong U$ is an immersion, proving both embedding assertions in (c).
:::

:::

::: {.pf-step #s7}
The surface $\Sigma$ has degree $\boxed{3}$.

::: pf-proof
Consider its hyperplane section $C=\Sigma\cap V_+(d-c)$.
On the chart $a=1$, the calculation in step [](#s6){.pf-ref} reduces to
$$
[a:b:c:d:e]=[1:u:u^2:u^2:u^3].
$$
On $e=1$, it reduces to
$$
[a:b:c:d:e]=[v^3:v^2:v:v:1].
$$
These two affine charts cover $C$: when $a=e=0$, the equations with $d=c$ force $b=c=d=0$, giving no projective point.
They glue with $v=u^{-1}$, and the formulas identify $C$ scheme-theoretically with the third Veronese embedding of $\PP^1$ in the hyperplane $d=c$.
In particular, $\OO_C(1)$ pulls back to $\OO_{\PP^1}(3)$, so its Hilbert polynomial is $P_C(n)=3n+1$, using $h^0(\PP^1,\OO(3n))=3n+1$ for $n\ge0$.

The hyperplane equation $d-c$ is nonzero on the integral surface $\Sigma$.
It gives the exact sequence
$$
0\longrightarrow\OO_\Sigma(n-1)\longrightarrow\OO_\Sigma(n)
\longrightarrow\OO_C(n)\longrightarrow0.
$$
For sufficiently large $n$, Serre vanishing and the Hilbert-polynomial comparison give
$$
P_\Sigma(n)-P_\Sigma(n-1)=P_C(n)=3n+1
$$
[@Har10a, Theorem III.5.2 and Exercise III.5.2].
The leading term of the Hilbert polynomial of a surface is $(\deg\Sigma)n^2/2$; its first difference has leading term $(\deg\Sigma)n$.
Comparing with $3n+1$ proves the degree claim.
:::

:::

::: {.pf-step #s8}
The strict transforms of the lines through $P$ are disjoint straight lines on $\Sigma$, and they form a ruling of the surface.

::: pf-proof
The second projection $\rho:B\to\PP^1$ sends $([x:y:z],[s:t])$ to $[s:t]$.
Over any extension field $K/k$, its fibre over a $K$-point $[1:u]$ is the strict transform of $y=ux$, parametrized by $[x:z]$.
Step [](#s5){.pf-ref} sends this fibre to
$$
[x:ux:u^2x:z:uz],
$$
the projective line spanned by the independent vectors $(1,u,u^2,0,0)$ and $(0,0,0,1,u)$.
The fibre over $[0:1]$ is treated on the other chart and maps to the line $[0:0:y:0:z]$.
Distinct fibres are disjoint on $B$, and their images remain disjoint because $j$ is an embedding.
The charts in step [](#s4){.pf-ref} identify $\rho$ locally with the projection $\AA^1\times\PP^1\to\AA^1$; thus they form a $\PP^1$-bundle covering the whole surface.
This proves the ruling assertion in every characteristic.
:::

:::

::: pf-qed
Step [](#s1){.pf-ref} proves (a).
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove the characteristic-dependent assertion (b).
Steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref}, and [](#s8){.pf-ref} give the immersion from $U$, its extension to the blowup, the degree, and the ruling required in (c).
:::

:::
:::

::: {.remark title="Characteristic and the fixed point"}
The specified five conics in the retained statement of part (b) do not give an immersion in characteristic two; step [](#s3){.pf-ref} gives an explicit counterexample.
The characteristic restriction is unnecessary in (a) and (c).
For a field not assumed algebraically closed, the point in (c) is required to be $k$-rational so that its conics form the stated five-dimensional system; over an algebraically closed field every closed point has this property.
:::
