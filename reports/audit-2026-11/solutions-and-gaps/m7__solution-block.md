::: {.solution}
By a similarity of $\CC$ we may suppose that $L=\RR$, oriented so that $\Omega_l$ is the part of $\Omega$ in the open upper half-plane:
$$
\Omega_l=\Omega\cap\{\Im z>0\},\qquad \Omega_r=\Omega\cap\{\Im z<0\},\qquad I=\Omega\cap\RR .
$$
A similarity carries curves to curves and homotopies to homotopies, so it suffices to prove the claim in this normalization. Since $I$ is an interval of the line $\RR$ it is convex, and $I\subseteq\Omega$; also $I\neq\varnothing$, because $L$ meets $\Omega$. The boundedness of $\Omega$ is not used below.

Curves are continuous maps on closed intervals, and a region is simply connected if any two curves in it with the same endpoints are homotopic in it (Chapter 3, §5). Every curve is parametrized on $[0,1]$, by composing with an affine reparametrization where necessary. For curves $\gamma,\eta$ with the same endpoints, $\gamma\simeq\eta$ means that they are homotopic in $\Omega$ with the endpoints held fixed; $\gamma*\eta$ is the concatenation, $\gamma^{-1}$ the reversed curve, and $c_x$ the constant curve at $x$. The argument of Example 1 in Chapter 3, §5 — the linear interpolation $H(u,t)=(1-u)\gamma_0(t)+u\gamma_1(t)$ — uses only convexity, so it applies to every convex set $K\subseteq\CC$, open or not: any two curves in $K$ with the same endpoints are homotopic in $K$. Below this is applied to the interval $I$, to open balls, to $\Omega_l$ and $\Omega_r$, whose simple connectivity is the hypothesis, and to the sets $W$ and $W\cap\Omega_l$ introduced in step [](#tube){.pf-ref}.

::: pf

::: {.pf-step #concat}
For curves in $\Omega$ with the indicated endpoints:
(i) $\gamma*\gamma^{-1}$ is homotopic to $c_{\gamma(0)}$;
(ii) $c*\gamma\simeq\gamma\simeq\gamma*c'$ for constant curves $c$ at the initial point and $c'$ at the terminal point of $\gamma$;
(iii) $(\gamma_1*\gamma_2)*\gamma_3\simeq\gamma_1*(\gamma_2*\gamma_3)$;
(iv) $\gamma\simeq\gamma'$ implies $\eta*\gamma*\theta\simeq\eta*\gamma'*\theta$ and $\gamma^{-1}\simeq\gamma'^{-1}$;
(v) $\gamma\circ\varphi\simeq\gamma$ for every increasing homeomorphism $\varphi$ of $[0,1]$.

::: pf-proof
For (i), the map $H(u,t)=\gamma\bigl((1-u)\min(2t,2-2t)\bigr)$ is continuous on $[0,1]^2$, takes the value $\gamma(0)$ at $t=0$ and at $t=1$, equals $(\gamma*\gamma^{-1})(t)=\gamma(\min(2t,2-2t))$ at $u=0$, and equals $c_{\gamma(0)}$ at $u=1$.
For (v), $H(u,t)=\gamma\bigl((1-u)\varphi(t)+ut\bigr)$ is continuous and fixes the endpoints, since $\varphi(0)=0$ and $\varphi(1)=1$.
For (ii) and (iii), $c*\gamma$, $\gamma*c'$ and the two bracketings of $\gamma_1*\gamma_2*\gamma_3$ are the curves $\gamma\circ\varphi$ for piecewise linear increasing maps $\varphi$ of $[0,1]$ onto itself, so (v) applies.
For (iv), the curve $(u,t)\mapsto\bigl(\eta*\gamma_u*\theta\bigr)(t)$ whose middle third is $\gamma_u$ is continuous on $[0,1]^2$ and fixes the endpoints, and $(u,t)\mapsto H(u,1-t)$ is a homotopy from $\gamma^{-1}$ to $\gamma'^{-1}$.
:::

:::

::: {.pf-step #polygonal}
Every curve $\gamma$ in $\Omega$ is homotopic in $\Omega$ to a polygonal curve with the same endpoints, the endpoints staying fixed.

::: pf-proof
Let $\gamma\colon J\to\Omega$ with $J=[a,b]$ and $K=\gamma(J)$, a compact subset of $\Omega$. There is $\varepsilon>0$ such that the ball $B(z,3\varepsilon)$ is contained in $\Omega$ for every $z\in K$: otherwise there are $z_n\in K$ and $w_n\notin\Omega$ with $\abs{z_n-w_n}<1/n$, a subsequence $z_{n_k}$ converges to a point $z\in K\subseteq\Omega$, and then $w_{n_k}\to z$ with $z\in\Omega^c$ because $\Omega^c$ is closed, which is impossible. This is the covering argument of the proof of Theorem 5.1 in Chapter 3, §5.

By uniform continuity choose $a=t_0<t_1<\cdots<t_N=b$ with $\abs{\gamma(t)-\gamma(t_k)}<\varepsilon$ for $t\in[t_k,t_{k+1}]$, put $z_k=\gamma(t_k)$, and let $P$ be the polygonal curve through $z_0,\dots,z_N$. For $t\in[t_k,t_{k+1}]$ put $\tau=(t-t_k)/(t_{k+1}-t_k)$ and
$$
H(u,t)=(1-u)\gamma(t)+u\bigl((1-\tau)z_k+\tau z_{k+1}\bigr).
$$
The points $\gamma(t)$ and $(1-\tau)z_k+\tau z_{k+1}$ both lie in $B(z_k,\varepsilon)$, the second because $\abs{z_{k+1}-z_k}<\varepsilon$, so $H(u,t)\in B(z_k,\varepsilon)\subseteq B(z_k,3\varepsilon)\subseteq\Omega$: the ball is convex, because $\abs{(1-u)x+uy-z}\le(1-u)\abs{x-z}+u\abs{y-z}$ for $x,y\in B(z,\varepsilon)$. At $t=t_k$ both terms of the convex combination equal $z_k$, so the pieces agree at the joins and $H$ is continuous on $[0,1]\times J$; moreover $H(0,\cdot)=\gamma$, $H(1,\cdot)=P$ and $H(u,a)=\gamma(a)$, $H(u,b)=\gamma(b)$ for all $u$.
:::

:::

::: {.pf-step #generic}
Let $P$ be a polygonal closed curve in $\Omega$. Then $P$ is freely homotopic in $\Omega$ to a polygonal closed curve $P'$ with no vertex on $L$ and no side parallel to $L$. Consequently $P'$ meets $L$ in finitely many points, each lying in the relative interior of a side, and at each of them $P'$ passes from one open half-plane into the other.

::: pf-proof
Let $v_0,\dots,v_{n-1}$ be the vertices of $P$ in order, with sides $[v_k,v_{k+1}]$ and $v_n=v_0$. The set $K=\abs{P}$ is compact and disjoint from the closed set $\Omega^c$, so $\delta=\dist(K,\Omega^c)>0$: otherwise there are $z_n\in K$ with $\dist(z_n,\Omega^c)<1/n$ and a subsequence $z_{n_k}\to z\in K\subseteq\Omega$, whence $\dist(z,\Omega^c)=0$ and $z\in\Omega^c$, which is impossible. Fix $0<\rho<\delta$ and, for real $s_0,\dots,s_{n-1}$ with $\abs{s_k}<\rho/2$, put $w_k=is_k$, $v'_k=v_k+w_k$ and $v'_n=v'_0$, and let $P'$ be the polygon through $v'_0,\dots,v'_{n-1}$.

Every point of the side $[v'_k,v'_{k+1}]$ is of the form $(1-\tau)v_k+\tau v_{k+1}+(1-\tau)w_k+\tau w_{k+1}$ with $0\le\tau\le1$, hence lies at distance less than $\rho$ from $[v_k,v_{k+1}]\subseteq K$; so $P'$ has image in $W_0=\{z:\dist(z,K)<\rho\}\subseteq\Omega$, because $\rho<\delta$. Parametrize $P$ and $P'$ affinely on corresponding sides; then $P'(t)-P(t)$ is the same convex combination of $w_0,\dots,w_{n-1}$ as $P(t)$ is of $v_0,\dots,v_{n-1}$, so $\abs{P'(t)-P(t)}\le\max_k\abs{w_k}<\rho$ and the linear interpolation $(1-u)P(t)+uP'(t)$ has image in $W_0\subseteq\Omega$. It is continuous on $[0,1]^2$ and closed for every $u$, so it is a free homotopy from $P$ to $P'$.

It remains to choose $s_0,\dots,s_{n-1}$. The requirements are $\Im v'_k=\Im v_k+s_k\neq0$ for all $k$ and $\Im(v'_{k+1}-v'_k)=\Im(v_{k+1}-v_k)+s_{k+1}-s_k\neq0$ for all $k$. With $s_k=t^{k+1}$, the $k$-th condition of the first family reads $\Im v_k+t^{k+1}=0$, and the $k$-th condition of the second reads $\Im(v_{k+1}-v_k)+t^{k+2}-t^{k+1}=0$ for $k<n-1$ and $\Im(v_0-v_{n-1})+t-t^n=0$ for $k=n-1$; each is a nonzero polynomial equation in $t$ of degree at most $n$, so each rules out at most $n$ values of $t$; choosing $t\neq0$ small enough and outside that finite set gives all of them together with $\abs{s_k}<\rho/2$.

Finally, a side of $P'$ joins two points off $L$ and is not parallel to $L$, so it meets $L$ in at most one point, and when it does the two halves of the side near that point lie in different open half-planes. Since no vertex lies on $L$, the finitely many intersection points lie in relative interiors of sides, and $P'$ passes from one open half-plane into the other at each of them.
:::

:::

::: {.pf-step #free-based}
A closed curve in $\Omega$ that is freely homotopic in $\Omega$ to a constant curve is homotopic to the constant curve at its own base point, the base point staying fixed.

::: pf-proof
Let $\eta$ be a closed curve with base point $x=\eta(0)$ and let $H\colon[0,1]^2\to\Omega$ satisfy $H(0,t)=\eta(t)$, $H(1,t)=w$ for a point $w$, and $H(u,0)=H(u,1)$ for every $u$. Then $\lambda(u)=H(u,0)$ is a curve from $x$ to $w$. Define
$$
G(u,t)=
\begin{cases}
\lambda(3t), & 0\le t\le u/3,\\
H\Bigl(u,\dfrac{t-u/3}{1-2u/3}\Bigr), & u/3\le t\le 1-u/3,\\
\lambda(3-3t), & 1-u/3\le t\le 1 .
\end{cases}
$$
The denominators are positive because $1-2u/3\ge1/3$, the three formulas agree at the joins $t=u/3$ and $t=1-u/3$, where they equal $\lambda(u)$, and $G(u,0)=G(u,1)=\lambda(0)=x$ for every $u$; hence $G$ is a homotopy of curves with fixed base point. At $u=0$ the middle formula covers $t\in[0,1]$ and gives $G(0,\cdot)=\eta$. At $u=1$ the three formulas give $\lambda$, then $c_w$, then $\lambda^{-1}$, so $\eta\simeq\lambda*c_w*\lambda^{-1}$, and this is homotopic to $c_x$: (ii) gives $\lambda*c_w\simeq\lambda$, hence $\lambda*c_w*\lambda^{-1}\simeq\lambda*\lambda^{-1}$ by (iv), and then $\lambda*\lambda^{-1}\simeq c_x$ by (i) of step [](#concat){.pf-ref}.
:::

:::

::: {.pf-step #crosscut}
Let $p,q\in I$, let $A\colon[0,1]\to\Omega$ be a curve with $A(0)=p$, $A(1)=q$ and $A\bigl((0,1)\bigr)$ contained in one of $\Omega_l,\Omega_r$, and let $s(t)=(1-t)p+tq$ be the segment from $p$ to $q$. Then $A*s^{-1}$ is null-homotopic at $p$ in $\Omega$, and consequently $A\simeq s$.

::: pf-proof

Assume $A\bigl((0,1)\bigr)\subseteq\Omega_l$; the other case is the same with $\Omega_r$ and the lower half-plane, all occurrences of $\Omega_l$ below being replaced by $\Omega_r$.

::: {.pf-step #tube}
With $K=[p,q]$ and $\rho>0$ so small that $\dist(K,\Omega^c)>\rho$, the set $W=\{z:\dist(z,K)<\rho\}$ is open and convex, $K\subseteq W\subseteq\Omega$, and $W\cap\Omega_l$ is convex.

::: pf-proof
$K$ is compact and disjoint from the closed set $\Omega^c$, so $\dist(K,\Omega^c)>0$, as in step [](#generic){.pf-ref}. $W$ is a union of open balls, hence open. If $z_j=k_j+b_j$ with $k_j\in K$ and $\abs{b_j}<\rho$ for $j=1,2$, then for $0\le\lambda\le1$
$$
\lambda z_1+(1-\lambda)z_2=\bigl(\lambda k_1+(1-\lambda)k_2\bigr)+\bigl(\lambda b_1+(1-\lambda)b_2\bigr),
$$
where the first summand lies in $K$, which is convex, and the second has modulus less than $\rho$; so $z_1,z_2\in W$ implies $\lambda z_1+(1-\lambda)z_2\in W$. For $z\in W$ choose $k\in K$ with $\abs{z-k}<\rho<\dist(K,\Omega^c)$; then $z\notin\Omega^c$, so $W\subseteq\Omega$. Finally $W\cap\Omega_l=W\cap\{\Im z>0\}$ is convex as the intersection of two convex sets.
:::

:::

::: {.pf-step #decompose}
There are numbers $0<t_0<t_1<1$ such that, with $\alpha=\restrictionof{A}{[0,t_0]}$, $\mu=\restrictionof{A}{[t_0,t_1]}$, $\gamma=\restrictionof{A}{[t_1,1]}$, $a_0=A(t_0)$ and $a_1=A(t_1)$, the images of $\alpha$ and of $\gamma$ lie in $W$, the image of $\mu$ lies in $\Omega_l$, and $a_0,a_1\in W\cap\Omega_l$; moreover $A=\alpha*\mu*\gamma$ up to reparametrization.

::: pf-proof
$A(0)=p\in K\subseteq W$ and $W$ is open, so $A(t)\in W$ for all $t$ in some interval $[0,t_0]$ with $0<t_0<1$. Likewise $A(t)\in W$ for all $t$ in some interval $[t_1,1]$, and $t_1$ may be taken larger than $t_0$ and smaller than $1$. Since $t_0,t_1\in(0,1)$, the points $a_0,a_1$ lie in $A\bigl((0,1)\bigr)\subseteq\Omega_l$ and a fortiori in $W$; and $A([t_0,t_1])\subseteq\Omega_l$. The identity $A=\alpha*\mu*\gamma$ holds up to the affine reparametrization of $[0,1]$.
:::

:::

::: {.pf-step #tau-rho}
Let $\rho_2$ be the segment from $a_1$ to $a_0$ and $\rho_3=\rho_2*\alpha^{-1}$. Then $\rho_2$ has image in $W\cap\Omega_l$, the curves $\tau=\gamma*s^{-1}$ and $\rho_3$ are curves in $W$ from $a_1$ to $p$, and $\tau\simeq\rho_3$ in $\Omega$ with endpoints fixed.

::: pf-proof
The segment $s$ has image in $K\subseteq W$ and $\gamma$ has image in $W$, so $\tau$ has image in $W$. The points $a_0,a_1$ lie in $W\cap\Omega_l$, which is convex by step [](#tube){.pf-ref}, so $\rho_2$ has image in $W\cap\Omega_l$; and $\alpha$ has image in $W$, so $\rho_3$ has image in $W$. Both $\tau$ and $\rho_3$ are curves in the convex set $W$ from $a_1$ to $p$, so the linear interpolation between them is a homotopy in $W\subseteq\Omega$ that keeps the endpoints fixed.
:::

:::

::: {.pf-step #loop}
The curve $A*s^{-1}$ is null-homotopic at $p$ in $\Omega$, and $A\simeq s$ with endpoints fixed.

::: pf-proof
Since $A*s^{-1}=\alpha*\mu*\gamma*s^{-1}=\alpha*\mu*\tau$ up to reparametrization, steps [](#tau-rho){.pf-ref} and [](#concat){.pf-ref} give
$$
A*s^{-1}\simeq\alpha*\mu*\rho_3=\alpha*\mu*\rho_2*\alpha^{-1}\simeq\alpha*(\mu*\rho_2)*\alpha^{-1}.
$$
The curve $\mu*\rho_2$ is a closed curve in $\Omega_l$ with base point $a_0$, so it is homotopic in the simply connected region $\Omega_l$ to $c_{a_0}$; concatenating that homotopy with $\alpha$ and $\alpha^{-1}$ and applying [](#concat){.pf-ref} (iv) gives $\alpha*(\mu*\rho_2)*\alpha^{-1}\simeq\alpha*c_{a_0}*\alpha^{-1}$, which is $\simeq\alpha*\alpha^{-1}\simeq c_p$ by [](#concat){.pf-ref} (ii) and (i). Hence $A*s^{-1}$ is null-homotopic at $p$, and then $A\simeq(A*s^{-1})*s\simeq c_p*s\simeq s$ by [](#concat){.pf-ref} (ii) and (iii).
:::

:::

:::

:::

::: {.pf-step #arcs}
Let $P'$ be a polygonal closed curve in $\Omega$ with no vertex on $L$ and no side parallel to $L$, meeting $L$, and let $t_1<\cdots<t_m$ be the parameters with $P'(t_i)\in L$. Put $p_i=P'(t_i)$ and let $A_i$ be the subcurve of $P'$ from $p_i$ to $p_{i+1}$, with indices taken modulo $m$. Then $p_i\in I$, the image of the interior of $A_i$ lies in $\Omega_l$ or in $\Omega_r$, and $A_i\simeq s_i$ with endpoints fixed, where $s_i$ is the segment from $p_i$ to $p_{i+1}$.

::: pf-proof
The points $p_i=P'(t_i)$ lie in $P'([0,1])\subseteq\Omega$ and on $L=\RR$, so $p_i\in I$. For $i<m$ the interior of $A_i$ is traversed on the interval $(t_i,t_{i+1})$, where $P'$ misses $L$, so its image is connected, being a continuous image of an interval, and is contained in one of the two components $\{\Im z>0\}$, $\{\Im z<0\}$ of $\CC\setminus L$; being also contained in $\Omega$, it lies in $\Omega_l$ or in $\Omega_r$. The interior of $A_m$ is traversed on $(t_m,1)$ and on $(0,t_1)$, and each of these two images is connected and misses $L$ while having the base point $P'(0)=P'(1)$ in its closure; that point is a vertex of $P'$, hence off $L$. A connected set disjoint from $L$ lies in one of the two components of $\CC\setminus L$, and it cannot lie in the one whose closure misses the base point, so each image lies in the open half-plane containing $P'(0)$: in $\Omega_l$ if $\Im P'(0)>0$ and in $\Omega_r$ if $\Im P'(0)<0$. The hypotheses of step [](#crosscut){.pf-ref} therefore hold for $A=A_i$, $p=p_i$ and $q=p_{i+1}$ in every case, and give $A_i\simeq s_i$.
:::

:::

::: {.pf-step #assembly}
Every closed curve in $\Omega$ is freely homotopic in $\Omega$ to a constant curve, and hence null-homotopic at its base point.

::: pf-proof
Let $\gamma$ be a closed curve in $\Omega$. By step [](#polygonal){.pf-ref}, $\gamma$ is homotopic to a polygonal closed curve $P$ with endpoints fixed, and by step [](#generic){.pf-ref}, $P$ is freely homotopic to a polygonal closed curve $P'$ with no vertex on $L$ and no side parallel to $L$. If $P'$ misses $L$, then its image is connected, as a continuous image of an interval, and is contained in $\CC\setminus L$ and in $\Omega$, so it lies in $\Omega_l$ or in $\Omega_r$ and is null-homotopic there. Otherwise let $p_1,\dots,p_m$ and $A_1,\dots,A_m$ be as in step [](#arcs){.pf-ref}; then $P'$ is the concatenation $A_1*\cdots*A_m$ up to reparametrization, and step [](#arcs){.pf-ref} together with (iii) and (iv) of step [](#concat){.pf-ref} gives $A_1*\cdots*A_m\simeq s_1*\cdots*s_m$ with endpoints fixed. Each $s_i$ is a segment joining two points of $I$, so it has image in $I$ and $s_1*\cdots*s_m$ has image in the convex set $I\subseteq\Omega$; therefore $s_1*\cdots*s_m$ is homotopic in $I$ to its initial point. Hence $\gamma$ is freely homotopic to a constant curve, and step [](#free-based){.pf-ref} shows that it is null-homotopic at its base point.
:::

:::

::: pf-qed
Let $\gamma_0,\gamma_1$ be curves in $\Omega$ with the same endpoints. Then $\gamma_0*\gamma_1^{-1}$ is a closed curve in $\Omega$, so by step [](#assembly){.pf-ref} it is null-homotopic at its base point, and
$$
\gamma_0\simeq\gamma_0*\gamma_1^{-1}*\gamma_1\simeq c*\gamma_1\simeq\gamma_1
$$
with endpoints fixed, by (ii), (iii) and (iv) of step [](#concat){.pf-ref}. Any two curves in $\Omega$ with the same endpoints are therefore homotopic in $\Omega$, which is the definition of simple connectivity in Chapter 3, §5; so $\Omega$ is simply connected.
:::

:::

:::
