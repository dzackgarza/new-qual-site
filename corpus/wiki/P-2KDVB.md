---
schema: qual/card@1
id: P-2KDVB
kind: problem
title: To see that $\ZZ_m$ is a $\ZZ_{mk}$ module, we define an action
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homomorphisms
  - Cyclic Groups
relations: []
review: draft
---

::: problem
To see that $\ZZ_m$ is a $\ZZ_{mk}$ module, we define an action

\[
\begin{align*}
\ZZ_{mk} &\actson \ZZ_{m} \\
[x]_{mk} \actson [y]_m &\definedas [xy]_m
\end{align*}
\]

**This is a well-defined action**:

If $[x_1]_{mk} = [x_2]_{mk}$ are two representatives of the same equivalence class, then
$$
[x_1]_{mk} - [x_2]_{mk} = [x_1-x_2]_{mk} = [0]_{mk} \implies m \divides x_1 - x_2.
$$

But then
\[
\begin{align*}
([x_1]_{mk}\actson [y]_m) - ([x_2]_{mk} \actson [y]_m) 
&= [x_1 y]_m - [x_2 y]_m \\
&= [(x_1 - x_2)y]_m \\
&= [0]_m,
\end{align*}
\]

which shows that their resulting actions on $\ZZ_m$ are equal.

**This action yields a module structure:**

- $r.(x+y) = r.x + r.y$:
$$
[r]_{mk} \actson ([x]_m + [y]_m)  = [r]_{mk} \actson [x+y]_m = [r(x+y)]_m = [rx]_m + [ry]_m.
$$

- $(r+s).x = r.x + s.x$:
$$
[r]_{mk} + [s]_{mk} \actson [x]_m = [r + s]_{mk} \actson [x]_m = [(r+s)x]_m = [rx]_m + [sx]_m.
$$

- $(rs).x = r.s.x$:
\[
\begin{align*}
[r]_{mk} \cdot [s]_{mk} \actson [x]_m 
&= [rs]_{mk} \actson [x]_m \\
&= [(rs)x]_m  \\
&= [r]_{mk} \actson [sx]_m \\
&= [r]_{mk} \actson ( [s]_{mk} \actson [x]_m).
\end{align*}
\]

- $1.x = x$:
$$
[1]_{mk} \actson [x]_m = [1x]_m = [x]_m.
$$

$\ZZ_m^* \definedas \hom_{\ZZ_{mk}}(\ZZ_m, \ZZ_{mk}) \cong \ZZ_m$:

Define a map
\[
\begin{align*}
\phi: \hom_{\ZZ_{mk}}(\ZZ_m, \ZZ_{mk}) &\to \ZZ_m \\
f \mapsto [f([1]_m)]_m
\end{align*}
\]

**$\phi$ is a homomorphism**, as

\[
\begin{align*}
\phi(f + g) &= [(f+g)([1]_m)]_m \\
&= [f([1]_m) + g([1]_m)]_m  \\
&= [f([1]_m)]_m + [g([1]_m)]_m \\ \\
\phi([r]_{mk} \actson f) &= [[r]_{mk} f([1]_m)]_m \\
&= [r]_m \cdot [f([1]_m)]_m \\
&= [r]_{mk}\actson \phi(f).
\end{align*}
\]

**$\phi$ is injective**, as $[f([1]_m)]_m = [0]_m$, then for any $1 \leq \ell \leq m$, we have
\[
\begin{align*}
[f([\ell]_m)]_m &= [\ell f([1]_m)]_m \\
&= \ell [f([1]_m)]_m \\
&= \ell[0]_m \\
&= [0]_m
,\end{align*}
\]

so $f$ must be the zero map.

**$\phi$ is surjective**, since if $[\ell]_m \in \ZZ_m$, we can define
\[
\begin{align*}
f_\ell: \ZZ_m &\to \ZZ_{mk} \\
[1]_m &\mapsto [\ell]_{mk}
\end{align*}
\]

which makes sense and is well-defined because $\ZZ_m \injects \ZZ_{mk}$, and the map is defined on the generator.

So we have the desired bijection.
$\qed$
:::
