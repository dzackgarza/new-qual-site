## Title

## D. Zack Garza

Sunday $1 7 ^ { \mathrm { t h } }$ May, 2020

Contents   
1 Fall 2009 1   
2 Fall 2011 4   
3 Spring 2014 7   
4 Fall 2015 8   
5 Spring 2015 11   
6 Fall 2016 15

## 1 Fall 2009

1. (1) Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R .$ . Show that for $r < R ,$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1).

2. Let f be a continuous function in the region

$$
D = \{ z \left| \ | z | > R , 0 \leq \arg z \leq \theta \right. \} \quad \mathrm { w h e r e } \quad 1 \leq \theta \leq 2 \pi .
$$

If there exists k such that $\operatorname* { l i m } _ { z \to \infty } z f ( z ) = k$ for z in the region D. Show that

$$
\operatorname* { l i m } _ { R ^ { \prime } \longrightarrow \infty } \int _ { L } f ( z ) d z = i \theta k ,
$$

where $L$ is the part of the circle $| z | = R ^ { \prime }$ which lies in the region $D .$

3. Suppose that $f$ is an analytic function in the region D which contains the point a. Let

$F ( z ) = z - a - q f ( z )$ where q is a complex parameter.

(1) Let $K \subset D$ be a circle with the center at point a and also we assume that $f ( z ) \neq 0$ for $z \in K$ . Prove that the function F has one and only one zero $z = w$ on the closed disc K whose boundary is the circle K if $| q | < \operatorname* { m i n } _ { z \in K } { \frac { | z - a | } { | f ( z ) | } }$

(2) Let G(z) be an analytic function on the disk K. Apply the residue theorem to prove that $\frac { G ( w ) } { F ^ { \prime } ( w ) } = \frac { 1 } { 2 \pi i } \int _ { K } \frac { G ( z ) } { F ( z ) } d z$ , where w is the zero from (1).

(3) $\mathrm { I f } ~ z \in { K }$ , prove that the function $\displaystyle \frac { 1 } { F ( z ) }$ can be represented as a convergent series with respect to q: ${ \frac { 1 } { F ( z ) } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( q f ( z ) ) ^ { n } } { ( z - a ) ^ { n + 1 } } }$

4. Evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x .
$$

5. Let $f = u + i v$ be differentiable $\ ( \mathrm { i . e . } \ f ^ { \prime } ( z )$ exists) with continuous partial derivatives at a point $z = r e ^ { i \theta } , r \neq 0$ . Show that

$$
\frac { \partial u } { \partial r } = \frac { 1 } { r } \frac { \partial v } { \partial \theta } , \quad \frac { \partial v } { \partial r } = - \frac { 1 } { r } \frac { \partial u } { \partial \theta } .
$$

6. Show that $\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x = { \frac { \pi } { n \sin { \frac { a \pi } { n } } } }$ using complex analysis, $0 < a < n$ . Here n is a positive integer.

7. For $s > 0$ , the gamma function is defined by $\Gamma ( s ) = \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { s - 1 } d t .$

1. Show that the gamma function is analytic in the half-plane $\Re ( s ) > 0$ , and is still given there by the integral formula above.

2. Apply the formula in the previous question to show that

$$
\Gamma ( s ) \Gamma ( 1 - s ) = \frac { \pi } { \sin \pi s } .
$$

Hint: You may need $\Gamma ( 1 - s ) = t \int _ { 0 } ^ { \infty } e ^ { - v t } ( v t ) ^ { - s } d v \mathrm { f o r } t > 0 .$

8. Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra: If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree n, then it has n zeros in C.

9. Suppose f is entire and there exist $A , R > 0$ and natural number N such that

$$
| f ( z ) | \geq A | z | ^ { N } { \mathrm { ~ f o r ~ } } | z | \geq R .
$$

Show that

(i) f is a polynomial and

(ii) the degree of f is at least N .

10. Let $f : \mathbb { C } \to \mathbb { C }$ be an injective analytic (also called univalent) function. Show that there exist complex numbers $a \neq 0$ and b such that $ f ( z ) = a z + b . $

11. Let g be analytic for $| z | \le 1$ and $| g ( z ) | < 1 \ \mathrm { f o r } \ | z | = 1$

1. Show that g has a unique fixed point in $| z | < 1$

2. What happens if we replace $| g ( z ) | < 1$ with $| g ( z ) | \leq 1$ for $| z | = 1 2$ Give an example if (a) is not true or give an proof if (a) is still true.

3. What happens if we simply assume that f is analytic for $| z | < 1$ and $| f ( z ) | < 1$ for $| z | < 1 2$ Suppose that $f ( z ) \not \equiv z .$ . Can f have more than one fixed point in $| z | < 1 2$

Hint: The map $\psi _ { \alpha } ( z ) = { \frac { \alpha - z } { 1 - \bar { \alpha } z } }$ may be useful.

12. Find a conformal map from $D = \{ z : \ | z | < 1 , \ | z - 1 / 2 | > 1 / 2 \}$ to the unit disk $\ \Delta = \{ z :$ $| z | < 1 \}$

13. Let $f ( z )$ be entire and assume values of $f ( z )$ lie outside a bounded open set Ω. Show without using Picard’s theorems that $f ( z )$ is a constant.

(1) Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R$ . Show that for $r < R ,$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1).

14. Let f(z) be entire and assume that $f ( z ) \leq M | z | ^ { 2 }$ outside some disk for some constant M . Show that $f ( z )$ is a polynomial in z of degree $\leq 2$

15. Let $a _ { n } ( z )$ be an analytic sequence in a domain D such that $\sum _ { n = 0 } ^ { \infty } | a _ { n } ( z ) |$ converges uniformly on bounded and closed sub-regions of D. Show that $\sum _ { n = 0 } ^ { \infty } \left| a _ { n } ^ { \prime } ( z ) \right|$ converges uniformly on bounded and closed sub-regions of $D .$

16. Let $f ( z )$ be analytic in an open set Ω except possibly at a point $z _ { \mathrm { 0 } }$ inside Ω. Show that if $f ( z )$ is bounded in near $z _ { \mathrm { 0 } }$ , then $\int _ { \Delta } f ( z ) d z = 0$ for all triangles $\Delta$ in Ω.

17. Assume f is continuous in the region: $0 < | z - a | \leq R , \ 0 \leq \arg ( z - a ) \leq \beta _ { 0 } \ ( 0 < \beta _ { 0 } \leq 2 \pi )$ and the limit $\operatorname* { l i m } _ { z \to a } ( z - a ) f ( z ) = A $ exists. Show that

$$
\operatorname * { l i m } _ { r  0 } \int _ { \gamma _ { r } } f ( z ) d z = i A \beta _ { 0 } \ ,
$$

where $\gamma _ { r } : = \lbrace z \mid z = a + r e ^ { i t } , 0 \leq t \leq \beta _ { 0 } \rbrace$

18. Show that $f ( z ) = z ^ { 2 }$ is uniformly continuous in any open disk $| z | < R$ , where $R > 0$ is fixed, but it is not uniformly continuous on C.

19. (1) Show that the function $u = u ( x , y )$ given by

$$
u ( x , y ) = { \frac { e ^ { n y } - e ^ { - n y } } { 2 n ^ { 2 } } } \sin n x \quad { \mathrm { f o r ~ } } n \in \mathbf { N }
$$

is the solution on $D = \{ ( x , y ) ~ | x ^ { 2 } + y ^ { 2 } < 1 \}$ of the Cauchy problem for the Laplace equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 0 , \quad u ( x , 0 ) = 0 , \quad \frac { \partial u } { \partial y } ( x , 0 ) = \frac { \sin n x } { n } .
$$

(2) Show that there exist points $( x , y ) \in D$ such that $\operatorname* { l i m } _ { n \longrightarrow \infty } | u ( x , y ) | = \infty$

## 2 Fall 2011

1. (1) Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R$ . Show that for $r < R ,$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1).

2. Let f be a continuous function in the region

$$
D = \{ z \ | | z | > R , 0 \leq \arg Z \leq \theta \} \quad \mathrm { w h e r e } \quad 0 \leq \theta \leq 2 \pi .
$$

If there exists k such that $\operatorname* { l i m } _ { z \to \infty } z f ( z ) = k$ for z in the region D. Show that

$$
\operatorname* { l i m } _ { R ^ { \prime } \longrightarrow \infty } \int _ { L } f ( z ) d z = i \theta k ,
$$

where L is the part of the circle $| z | = R ^ { \prime }$ which lies in the region D.

3. Suppose that f is an analytic function in the region D which contains the point a. Let

$$
F ( z ) = z - a - q f ( z ) , \quad { \mathrm { w h e r e } } \quad q { \mathrm { ~ i s ~ a ~ c o m p l e x ~ p a r a m e t e r . } }
$$

(1) Let $K \subset D$ be a circle with the center at point a and also we assume that $f ( z ) \neq 0$ for $z \in K$ . Prove that the function F has one and only one zero $z = w$ on the closed disc K whose boundary is the circle K if $| q | < \operatorname* { m i n } _ { z \in K } { \frac { | z - a | } { | f ( z ) | } }$

(2) Let $G ( z )$ be an analytic function on the disk K. Apply the residue theorem to prove that $\frac { G ( w ) } { F ^ { \prime } ( w ) } = \frac { 1 } { 2 \pi i } \int _ { K } \frac { G ( z ) } { F ( z ) }$ dz, where w is the zero from (1).

(3) $\mathrm { I f } ~ z \in { K }$ , prove that the function $\displaystyle \frac { 1 } { F ( z ) }$ can be represented as a convergent series with respect to $q \colon { \frac { 1 } { F ( z ) } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( q f ( z ) ) ^ { n } } { ( z - a ) ^ { n + 1 } } }$

4. Evaluate $\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x$

5. Let $f = u + i v$ be differentiable $\ ( \mathrm { i . e . } \ f ^ { \prime } ( z )$ exists) with continuous partial derivatives at a point $z = r e ^ { i \theta } , r \neq 0$ . Show that

$$
\frac { \partial u } { \partial r } = \frac { 1 } { r } \frac { \partial v } { \partial \theta } , \quad \frac { \partial v } { \partial r } = - \frac { 1 } { r } \frac { \partial u } { \partial \theta } .
$$

6. Show that $\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x = { \frac { \pi } { n \sin { \frac { a \pi } { n } } } }$ using complex analysis, $0 < a < n$ . Here n is a positive integer.

7. For $s > 0$ , the gamma function is defined by $\Gamma ( s ) = \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { s - 1 } d t$

1. Show that the gamma function is analytic in the half-plane $\Re ( s ) > 0$ , and is still given there by the integral formula above.

2. Apply the formula in the previous question to show that

$$
\Gamma ( s ) \Gamma ( 1 - s ) = \frac { \pi } { \sin \pi s } .
$$

Hint: You may need $\Gamma ( 1 - s ) = t \int _ { 0 } ^ { \infty } e ^ { - v t } ( v t ) ^ { - s } d v \mathrm { f o r } t > 0 .$

8. Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra: If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree n, then it has n zeros in $\mathbb { C } .$

9. Suppose f is entire and there exist $A , R > 0$ and natural number N such that

$$
| f ( z ) | \geq A | z | ^ { N } { \mathrm { ~ f o r ~ } } | z | \geq R .
$$

Show that (i) f is a polynomial and (ii) the degree of f is at least N .

10. Let $f : \mathbb { C } \to \mathbb { C }$ be an injective analytic (also called univalent) function. Show that there exist complex numbers $a \neq 0$ and b such that $ f ( z ) = a z + b . $

11. Let g be analytic for $| z | \le 1$ and $| g ( z ) | < 1 \ \mathrm { f o r } \ | z | = 1$

• Show that g has a unique fixed point in $| z | < 1$

• What happens if we replace $| g ( z ) | < 1$ with $| g ( z ) | \leq 1$ for $| z | = 1 2$ Give an example if (a) is not true or give an proof if (a) is still true.

• What happens if we simply assume that f is analytic for $| z | < 1$ and $| f ( z ) | < 1$ for $| z | < 1 2$ Suppose that $f ( z ) \not \equiv z .$ . Can f have more than one fixed point in $| z | < 1 2$

Hint: The map $\psi _ { \alpha } ( z ) = { \frac { \alpha - z } { 1 - \bar { \alpha } z } }$ may be useful.

12. Find a conformal map from $D = \{ z : \ | z | < 1 , \ | z - 1 / 2 | > 1 / 2 \}$ to the unit disk $\ \Delta = \{ z :$ $| z | < 1 \}$

13. Let f(z) be entire and assume values of $f ( z )$ lie outside a bounded open set Ω. Show without using Picard’s theorems that $f ( z )$ is a constant.

14. Let $f ( z )$ be entire and assume values of $f ( z )$ lie outside a bounded open set Ω. Show without using Picard’s theorems that $f ( z )$ is a constant.

15. (1) Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R$ . Show that for $r < R$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1).

16. Let f(z) be entire and assume that $f ( z ) \leq M | z | ^ { 2 }$ outside some disk for some constant M . Show that f(z) is a polynomial in z of degree $\leq 2$

17. Let $a _ { n } ( z )$ be an analytic sequence in a domain D such that $\sum _ { n = 0 } ^ { \infty } | a _ { n } ( z ) |$ converges uniformly on bounded and closed sub-regions of D. Show that $\sum _ { n = 0 } ^ { \infty } \left| a _ { n } ^ { \prime } ( z ) \right|$ converges uniformly on bounded and closed sub-regions of D.

18. Let f(z) be analytic in an open set Ω except possibly at a point $z _ { \mathrm { 0 } }$ inside Ω. Show that if $f ( z )$ is bounded in near $z _ { \mathrm { 0 } }$ , then $\int _ { \Delta } f ( z ) d z = 0$ for all triangles $\Delta$ in Ω.

19. Assume f is continuous in the region: $0 < | z - a | \leq R , \ 0 \leq \arg ( z - a ) \leq \beta _ { 0 } \ ( 0 < \beta _ { 0 } \leq 2 \pi )$ and the limit $\operatorname* { l i m } _ { z \to a } ( z - a ) f ( z ) = A $ exists. Show that

$$
\operatorname * { l i m } _ { r  0 } \int _ { \gamma _ { r } } f ( z ) d z = i A \beta _ { 0 } \ ,
$$

where $\gamma _ { r } : = \lbrace z \mid z = a + r e ^ { i t } , 0 \leq t \leq \beta _ { 0 } \rbrace$

20. Show that $f ( z ) = z ^ { 2 }$ is uniformly continuous in any open disk $| z | < R$ , where $R > 0$ is fixed, but it is not uniformly continuous on C.

(1) Show that the function $u = u ( x , y )$ given by

$$
u ( x , y ) = { \frac { e ^ { n y } - e ^ { - n y } } { 2 n ^ { 2 } } } \sin n x \quad { \mathrm { f o r ~ } } n \in \mathbf { N }
$$

is the solution on $D = \{ ( x , y ) ~ | x ^ { 2 } + y ^ { 2 } < 1 \}$ of the Cauchy problem for the Laplace equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 0 , \quad u ( x , 0 ) = 0 , \quad \frac { \partial u } { \partial y } ( x , 0 ) = \frac { \sin n x } { n } .
$$

(2) Show that there exist points $( x , y ) \in D$ such that $\operatorname* { l i m } _ { n \longrightarrow \infty } | u ( x , y ) | = \infty$

## 3 Spring 2014

1. The question provides some insight into Cauchy’s theorem. Solve the problem without using the Cauchy theorem.

1. Evaluate the integral $\int _ { \gamma } z ^ { n } d z$ for all integers n. Here γ is any circle centered at the origin with the positive (counterclockwise) orientation.

2. Same question as (a), but with γ any circle not containing the origin.

3. Show that if $| a | < r < | b |$ , then $\int _ { \gamma } { \frac { d z } { ( z - a ) ( z - b ) } } d z = { \frac { 2 \pi i } { a - b } }$ . Here $\gamma$ denotes the circle centered at the origin, of radius r, with the positive orientation.

2. (1) Assume the infinite series $\sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R$ and let $f ( z )$ be the limit. Show that for $r < R$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1). Liouville’s theorem: If f (z) is entire and bounded, then $f$ is constant.

3. Let f be a continuous function in the region

$$
D = \{ z \ | | z | > R , 0 \leq \arg Z \leq \theta \} \quad \mathrm { w h e r e } \quad 0 \leq \theta \leq 2 \pi .
$$

If there exists k such that $\operatorname* { l i m } _ { z \to \infty } z f ( z ) = k$ for z in the region D. Show that

$$
\operatorname* { l i m } _ { R ^ { \prime } \longrightarrow \infty } \int _ { L } f ( z ) d z = i \theta k ,
$$

where L is the part of the circle $| z | = R ^ { \prime }$ which lies in the region D.

4. Evaluate $\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x$

5. Let $f = u + i v$ be differentiable $\ ( \mathrm { i . e . } \ f ^ { \prime } ( z )$ exists) with continuous partial derivatives at a point $z = r e ^ { i \theta } , r \neq 0$ . Show that

$$
\frac { \partial u } { \partial r } = \frac { 1 } { r } \frac { \partial v } { \partial \theta } , \quad \frac { \partial v } { \partial r } = - \frac { 1 } { r } \frac { \partial u } { \partial \theta } .
$$

6. Show that $\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x = { \frac { \pi } { n \sin { \frac { a \pi } { n } } } }$ using complex analysis, $0 < a < n$ . Here n is a positive integer.

7. For $s > 0$ , the gamma function is defined by $\Gamma ( s ) = \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { s - 1 } d t .$

• Show that the gamma function is analytic in the half-plane $\Re ( s ) > 0$ , and is still given there by the integral formula above.

• Apply the formula in the previous question to show that

$$
\Gamma ( s ) \Gamma ( 1 - s ) = \frac { \pi } { \sin \pi s } .
$$

Hint: You may need $\Gamma ( 1 - s ) = t \int _ { 0 } ^ { \infty } e ^ { - v t } ( v t ) ^ { - s } d v \mathrm { f o r } t > 0 .$

8. Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra: If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree n, then it has n zeros in C.

9. Suppose $f$ is entire and there exist $A , R > 0$ and natural number N such that

$$
| f ( z ) | \geq A | z | ^ { N } { \mathrm { ~ f o r ~ } } | z | \geq R .
$$

Show that (i) f is a polynomial and (ii) the degree of f is at least N .

10. Let $f : \mathbb { C } \to \mathbb { C }$ be an injective analytic (also called univalent) function. Show that there exist complex numbers $a \neq 0$ and b such that $ f ( z ) = a z + b$

11. Let g be analytic for $| z | \le 1$ and $| g ( z ) | < 1 \ \mathrm { f o r } \ | z | = 1$

• Show that g has a unique fixed point in $| z | < 1$

• What happens if we replace $| g ( z ) | < 1$ with $| g ( z ) | \leq 1$ for $| z | = 1 2$ Give an example if (a) is not true or give an proof if (a) is still true.

• What happens if we simply assume that f is analytic for $| z | < 1$ and $| f ( z ) | < 1$ for $| z | < 1 2$ Suppose that $f ( z ) \not \equiv z$ . Can f have more than one fixed point in $| z | < 1 2$

Hint: The map $\psi _ { \alpha } ( z ) = { \frac { \alpha - z } { 1 - \bar { \alpha } z } }$ may be useful.

12. Find a conformal map from $D = \{ z : \ | z | < 1 , \ | z - 1 / 2 | > 1 / 2 \}$ to the unit disk $\ \Delta = \{ z :$ $| z | < 1 \}$ .

## 4 Fall 2015

1. Let $a _ { n } \neq 0$ and assume that $\operatorname* { l i m } _ { n \to \infty } { \frac { | a _ { n + 1 } | } { | a _ { n } | } } = L$ . Show that $\operatorname* { l i m } _ { n \to \infty } \sqrt [ n ] { | a _ { n } | } = L$ . In particular, this shows that when applicable, the ratio test can be used to calculate the radius of convergence of a power series.

2. (a) Let $z , w$ be complex numbers, such that $\bar { z } w \ne 1$ . Prove that

$$
\left| { \frac { w - z } { 1 - { \overline { { w } } } z } } \right| < 1 \ \mathrm { ~ i f ~ } | z | < 1 \ \mathrm { a n d ~ } | w | < 1 ,
$$

and also that

$$
\left| { \frac { w - z } { 1 - \overline { { w } } z } } \right| = 1 \ \mathrm { ~ i f ~ } | z | = 1 \mathrm { ~ o r ~ } | w | = 1 .
$$

(b) Prove that for fixed w in the unit disk D, the mapping

$$
F : z \mapsto { \frac { w - z } { 1 - { \overline { { w } } } z } }
$$

satisfies the following conditions:

(c) F maps D to itself and is holomorphic.

(ii) F interchanges 0 and w, namely, $F ( 0 ) = w { \mathrm { ~ a n d ~ } } F ( w ) = 0$

(iii) $| F ( z ) | = 1 { \mathrm { ~ i f ~ } } | z | = 1 .$

(iv) $F : \mathbb { D } \mapsto \mathbb { D }$ is bijective.

Hint: Calculate $F \circ F .$

3. Use n-th roots of unity (i.e. solutions of $z ^ { n } - 1 = 0 )$ to show that

$$
2 ^ { n - 1 } \sin { \frac { \pi } { n } } \sin { \frac { 2 \pi } { n } } \cdot \cdot \cdot \sin { \frac { ( n - 1 ) \pi } { n } } = n .
$$

Hint: $1 - \cos 2 \theta = 2 \sin ^ { 2 } \theta , \sin 2 \theta = 2 \sin \theta \cos \theta .$

(a) Show that in polar coordinates, the Cauchy-Riemann equations take the form

$$
\frac { \partial u } { \partial r } = \frac { 1 } { r } \frac { \partial v } { \partial \theta } \mathrm { a n d } \frac { \partial v } { \partial r } = - \frac { 1 } { r } \frac { \partial u } { \partial \theta }
$$

(b) Use these equations to show that the logarithm function defined by

$$
\log z = \log r + i \theta \mathrm { \ w h e r e \ } z = r e ^ { i \theta } \mathrm { \ w i t h \ } - \pi < \theta < \pi
$$

is a holomorphic function in the region $r > 0 , - \pi < \theta < \pi$ . Also show that log z defined above is not continuous in $r > 0$

4. Assume $f$ is continuous in the region: x $\geq x _ { 0 } , \ 0 \leq y \leq b$ and the limit

$$
\operatorname* { l i m } _ { x  + \infty } f ( x + i y ) = A
$$

exists uniformly with respect to y (independent of $y )$ . Show that

$$
\operatorname* { l i m } _ { x  + \infty } \int _ { \gamma _ { x } } f ( z ) d z = i A b ,
$$

where $\gamma _ { x } : = \{ z \mid z = x + i t , 0 \leq t \leq b \}$

5. (Cauchy’s formula for “exterior” region) Let $\gamma$ be piecewise smooth simple closed curve with interior $\Omega _ { 1 }$ and exterior $\Omega _ { 2 }$ . Assume $f ^ { \prime } ( z )$ exists in an open set containing $\gamma$ and $\Omega _ { 2 }$ and lim $f ( z ) = A$ . Show that z→∞

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \xi ) } { \xi - z } } d \xi = { \left\{ \begin{array} { l l } { A , } & { { \mathrm { i f ~ } } z \in \Omega _ { 1 } , } \\ { - f ( z ) + A , } & { { \mathrm { i f ~ } } z \in \Omega _ { 2 } } \end{array} \right. }
$$

6. Let $f ( z )$ be bounded and analytic in C. Let $a \neq b$ be any fixed complex numbers. Show that the following limit exists

$$
\operatorname* { l i m } _ { R \to \infty } \int _ { | z | = R } { \frac { f ( z ) } { ( z - a ) ( z - b ) } } d z .
$$

Use this to show that $f ( z )$ must be a constant (Liouville’s theorem).

7. Prove by justifying all steps that for all $\xi \in \mathbb { C }$ we have $e ^ { - \pi \xi ^ { 2 } } = \int _ { - \infty } ^ { \infty } e ^ { - \pi x ^ { 2 } } e ^ { 2 \pi i x \xi } d x$

Hint: You may use that fact in Example 1 on p. 42 of the textbook without proof, i.e., you may assume the above is true for real values of $\xi .$

8. Suppose that f is holomorphic in an open set containing the closed unit disc, except for a pole at $z _ { \mathrm { 0 } }$ on the unit circle. Let denote the the power series in the open disc. Show that (1) $c _ { n } \neq 0$ for all large enough n’s, and (2) lim $\frac { c _ { n } } { c _ { n + 1 } } = z _ { 0 }$ n→∞

9. Let $f ( z )$ be a non-constant analytic function in $| z | > 0$ such that $f ( z _ { n } ) = 0$ for infinite many points $z _ { n }$ with $\operatorname* { l i m } _ { n \to \infty } z _ { n } = 0$ . Show that $z = 0$ is an essential singularity for $f ( z )$ . (An example of such a function is $f ( z ) = \sin ( 1 / z ) . )$

10. Let f be entire and suppose that $\operatorname* { l i m } _ { z \to \infty } f ( z ) = \infty$ . Show that f is a polynomial.

11. Expand the following functions into Laurent series in the indicated regions:

$$
{ \mathrm { ( a ) } } \ f ( z ) = { \frac { z ^ { 2 } - 1 } { ( z + 2 ) ( z + 3 ) } } , \ 2 < | z | < 3 , \ 3 < | z | < + \infty .
$$

$$
{ \mathrm { ( b ) } } \ f ( z ) = \sin { \frac { z } { 1 - z } } , \ 0 < | z - 1 | < + \infty
$$

12. Assume f (z) is analytic in region D and Γ is a rectifiable curve in D with interior in D. Prove that if f (z) is real for all $z \in \Gamma$ , then $f ( z )$ is a constant.

13. Find the number of roots of $z ^ { 4 } - 6 z + 3 = 0$ in $| z | < 1$ and $1 < | z | < 2$ respectively.

14. Prove that $z ^ { 4 } + 2 z ^ { 3 } - 2 z + 1 0 = 0$ has exactly one root in each open quadrant.

15. (1) Let $f ( z ) \in H ( \mathbb { D } ) , \operatorname { R e } ( f ( z ) ) > 0 , f ( 0 ) = a > 0$ . Show that

$$
| \frac { f ( z ) - a } { f ( z ) + a } | \leq | z | , | f ^ { \prime } ( 0 ) | \leq 2 a .
$$

(2) Show that the above is still true if $\mathrm { R e } ( f ( z ) ) > 0$ is replaced with $\mathrm { R e } ( f ( z ) ) \geq 0$

16. Assume $f ( z )$ is analytic in D and $f ( 0 ) = 0$ and is not a rotation $( { \mathrm { i . e . ~ } } f ( z ) \neq e ^ { i \theta } z )$ . Show that $\sum _ { n = 1 } ^ { \infty } f ^ { n } ( z )$ converges uniformly to an analytic function on compact subsets of D, where $f ^ { n + 1 } ( z ) = f ( f ^ { n } ( z ) )$

17. Let $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ be analytic and one-to-one in $| z | < 1$ . For $0 < r < 1$ , let $D _ { r }$ be the disk

$| z | < r$ . Show that the area of $f ( D _ { r } )$ is finite and is given by

$$
S = \pi \sum _ { n = 1 } ^ { \infty } n | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(Note that in general the area of $f ( D _ { 1 } )$ is infinite.)

18. Let $f ( z ) = \sum _ { n = - \infty } ^ { \infty } c _ { n } z ^ { n }$ be analytic and one-to-one in $r _ { 0 } < | z | < R _ { 0 }$ . For $r _ { 0 } < r < R < R _ { 0 }$ , let $D ( r , R )$ be the annulus $r < | z | < R$ . Show that the area of $f ( D ( r , R ) )$ is finite and is given by

$$
S = \pi \sum _ { n = - \infty } ^ { \infty } n | c _ { n } | ^ { 2 } ( R ^ { 2 n } - r ^ { 2 n } ) .
$$

## 5 Spring 2015

1. Let $a _ { n } ( z )$ be an analytic sequence in a domain D such that $\sum _ { n = 0 } ^ { \infty } | a _ { n } ( z ) |$ converges uniformly on bounded and closed sub-regions of D. Show that $\sum _ { n = 0 } ^ { \infty } \left| a _ { n } ^ { \prime } ( z ) \right|$ converges uniformly on bounded and closed sub-regions of D.

2. Let $f _ { n } , f$ be analytic functions on the unit disk D. Show that the following are equivalent.

(i) $f _ { n } ( z )$ converges to f(z) uniformly on compact subsets in D.

(ii) $\int _ { | z | = r } | f _ { n } ( z ) - f ( z ) | | d z |$ converges to 0 if $0 < r < 1$

3. Let f and g be non-zero analytic functions on a region Ω. Assume $| f ( z ) | = | g ( z ) |$ for all z in Ω. Show that $f ( z ) = e ^ { i \theta } g ( z )$ in Ω for some $0 \leq \theta < 2 \pi$ .

4. Suppose f is analytic in an open set containing the unit disc D and $| f ( z ) | = 1$ when $| z | { = } 1$ Show that either ${ \dot { f } } ( z ) = e ^ { i \theta }$ for some $\theta \in \mathbb { R }$ or there are finite number of $z _ { k } \in \mathbb { D } , k \le n$ and $\theta \in \mathbb { R }$ such that $f ( z ) = e ^ { i \theta } \prod _ { k = 1 } ^ { n } { \frac { z - z _ { k } } { 1 - { \bar { z } } _ { k } z } }$

Also cf. Stein et al, 1.4.7, 3.8.17

5. (1) Let $p ( z )$ be a polynomial, $R > 0$ any positive number, and $m \geq 1$ an integer. Let $M _ { R } = \operatorname* { s u p } \{ | z ^ { m } p ( z ) - 1 | : | z | = R \}$ . Show that $M _ { R } > 1$ •

(2) Let $m \geq 1$ be an integer and $K = \{ z \in \mathbb { C } : r \leq | z | \leq R \}$ where $r < R .$ . Show (i) using (1) as well as, (ii) without using (1) that there exists a positive number $\varepsilon _ { 0 } > 0$ such that for each polynomial $p ( z )$ ,

$$
\operatorname* { s u p } \{ | p ( z ) - z ^ { - m } | : z \in K \} \geq \varepsilon _ { 0 } .
$$

6. Let $f ( z ) = { \frac { 1 } { z } } + { \frac { 1 } { z ^ { 2 } - 1 } }$ . Find all the Laurent series of f and describe the largest annuli in which these series are valid.

7. Suppose f is entire and there exist A, $R > 0$ and natural number N such that $| f ( z ) | \leq A | z | ^ { N }$ for $| z | \geq R .$ . Show that (i) f is a polynomial and (ii) the degree of f is at most N .

8. Suppose f is entire and there exist A, $R > 0$ and natural number N such that $| f ( z ) | \geq A | z | ^ { N }$ for $| z | \geq R$ . Show that (i) f is a polynomial and (ii) the degree of f is at least N .

9. (1) Explicitly write down an example of a non-zero analytic function in $| z | < 1$ which has infinitely zeros in $| z | < 1$ .

(2) Why does not the phenomenon in (1) contradict the uniqueness theorem?

10. (1) Assume u is harmonic on open set O and $z _ { n }$ is a sequence in O such that $u ( z _ { n } ) = 0$ and lim $z _ { n } \in O$ . Prove or disprove that u is identically zero. What if O is a region?

(2) Assume u is harmonic on open set O and $u ( z ) = 0$ on a disc in O. Prove or disprove that u is identically zero. What if O is a region?

(3) Formulate and prove a Schwarz reflection principle for harmonic functions

cf. Theorem 5.6 on p.60 of Stein et al.

Hint: Verify the mean value property for your new function obtained by Schwarz reflection principle.

11. Let f be holomorphic in a neighborhood of $D _ { r } ( z _ { 0 } )$ . Show that for any $s < r _ { : }$ , there exists a constant $c > 0$ such that

$$
\| f \| _ { ( \infty , s ) } \leq c \| f \| _ { ( 1 , r ) } ,
$$

where $| f | | _ { ( \infty , s ) } = \operatorname* { s u p } _ { z \in D _ { s } ( z _ { 0 } ) } | f ( z ) | \mathrm { ~ a n d ~ } | | f | | _ { ( 1 , r ) } = \int _ { D _ { r } ( z _ { 0 } ) } | f ( z ) | d x d y .$

Note: Exercise 3.8.20 on p.107 in Stein et al is a straightforward consequence of this stronger result using the integral form of the Cauchy-Schwarz inequality in real analysis.

12. (1) Let f be analytic in $\Omega : 0 < | z - a | < r$ except at a sequence of poles $a _ { n } \in \Omega$ with $\operatorname* { l i m } _ { n \to \infty } a _ { n } = a $ . Show that for any w $\in \mathbb { C }$ , there exists a sequence $z _ { n } \in \Omega$ such that $\operatorname* { l i m } _ { n \to \infty } f ( z _ { n } ) = w$

(2) Explain the similarity and difference between the above assertion and the Weierstrass-Casorati theorem.

13. Compute the following integrals.

$$
( \mathrm { i } ) \int _ { 0 } ^ { \infty } \frac { 1 } { ( 1 + x ^ { n } ) ^ { 2 } } d x , n \geq 1 \ ( \mathrm { i i } ) \int _ { 0 } ^ { \infty } \frac { \cos x } { ( x ^ { 2 } + a ^ { 2 } ) ^ { 2 } } d x , a \in \mathbb { R } \ ( \mathrm { i i i } ) \int _ { 0 } ^ { \pi } \frac { 1 } { a + \sin \theta } d \theta , a > 1
$$

$$
( \mathrm { i v } ) \int _ { 0 } ^ { \frac { \pi } { 2 } } \frac { d \theta } { a + \sin ^ { 2 } \theta } , \mathrm { ~ } a > 0 . \left( \mathrm { v } \right) \int _ { | z | = 2 } \frac { 1 } { \left( z ^ { 5 } - 1 \right) \left( z - 3 \right) } d z \left( \mathrm { v } \right) \int _ { - \infty } ^ { \infty } \frac { \sin \pi a } { \cosh \pi x + \cos \pi a } e ^ { - i x \xi } d x ,
$$

$$
0 < a < 1 , \xi \in \mathbb { R } { \mathrm { ~ ( v i ) ~ } } \int _ { | z | = 1 } { \cot ^ { 2 } z d z } .
$$

14. Compute the following integrals.

$$
( \mathrm { i } ) \int _ { 0 } ^ { \infty } \frac { \sin { x } } { x } d x \ \mathrm { ( i i ) } \int _ { 0 } ^ { \infty } ( \frac { \sin { x } } { x } ) ^ { 2 } d x \ \mathrm { ( i i i ) } \int _ { 0 } ^ { \infty } \frac { x ^ { a - 1 } } { ( 1 + x ) ^ { 2 } } d x , 0 < a < 2
$$

$$
\int _ { 0 } ^ { \infty } \frac { \cos a x - \cos b x } { x ^ { 2 } } d x , a , b > 0 \mathrm { ( i i ) } \int _ { 0 } ^ { \infty } \frac { x ^ { a - 1 } } { 1 + x ^ { n } } d x , 0 < a < n
$$

$$
( \mathrm { i i i } ) \int _ { 0 } ^ { \infty } { \frac { \log { x } } { 1 + x ^ { n } } } d x , n \geq 2 \ ( \mathrm { i v } ) \int _ { 0 } ^ { \infty } { \frac { \log { x } } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x \ ( \mathrm { v } ) \int _ { 0 } ^ { \pi } \log \left| 1 - a \sin \theta \right| d \theta , a \in \mathbb { C }
$$

15. Let $0 < r < 1$ . Show that polynomials $P _ { n } ( z ) = 1 + 2 z + 3 z ^ { 2 } + \cdot \cdot \cdot + n z ^ { n - 1 }$ have no zeros in $| z | < r$ for all sufficiently large n’s.

16. Let f be an analytic function on a region Ω. Show that f is a constant if there is a simple closed curve γ in Ω such that its image $f ( \gamma )$ is contained in the real axis.

17. (1) Show that ${ \frac { \pi ^ { 2 } } { \sin ^ { 2 } \pi z } } \operatorname { a n d } g ( z ) = \sum _ { n = - \infty } ^ { \infty } { \frac { 1 } { ( z - n ) ^ { 2 } } }$ have the same principal part at each integer point.

(2) Show that $h ( z ) ~ = ~ \frac { \pi ^ { 2 } } { \sin ^ { 2 } \pi z } - g ( z )$ is bounded on C and conclude that $\frac { \pi ^ { 2 } } { \sin ^ { 2 } \pi z } =$ $\sum _ { n = - \infty } ^ { \infty } \frac { 1 } { ( z - n ) ^ { 2 } } .$

18. Let $f ( z )$ be an analytic function on $\mathbb { C } \backslash \{ z _ { 0 } \}$ , where $z _ { \mathrm { 0 } }$ is a fixed point. Assume that $f ( z )$ is bijective from $\mathbb { C } \backslash \{ z _ { 0 } \}$ onto its image, and that $f ( z )$ is bounded outside $D _ { r } ( z _ { 0 } )$ , where r is some fixed positive number. Show that there exist $a , b , c , d \in \mathbb { C }$ with $a d - b c \neq 0 , c \neq 0$ such that $f ( z ) = { \frac { a z + b } { c z + d } } .$

19. Assume $f ( z )$ is analytic in $\mathbb { D } : | z | < 1$ and $f ( 0 ) = 0$ and is not a rotation $( { \mathrm { i . e . ~ } } f ( z ) \neq e ^ { i \theta } z )$ Show that $\sum ^ { \infty } f ^ { n } ( z )$ converges uniformly to an analytic function on compact subsets of D, where ${ f ^ { n + 1 } } ( z ) = f ( f ^ { n } ( z ) )$

20. Let f be a non-constant analytic function on D with $f ( \mathbb { D } ) \subseteq \mathbb { D } . { \mathrm { ~ U s e ~ } } \psi _ { a } ( f ( z ) )$ (where $a = f ( 0 )$ $\psi _ { a } ( z ) = \frac { a - z } { 1 - \bar { a } z } )$ to prove that ${ \frac { | f ( 0 ) | - | z | } { 1 + | f ( 0 ) | | z | } } \leq | f ( z ) | \leq { \frac { | f ( 0 ) | + | z | } { 1 - | f ( 0 ) | | z | } } ,$

21. Find a conformal map

1. from $\{ z : | z - 1 / 2 | > 1 / 2 , { \mathrm { R e } } ( z ) > 0 \}$ to H

2. from $\left\{ z : | z - 1 / 2 | > 1 / 2 , | z | < 1 \right\}$ to D

3. from the intersection of the disk $| z + i | < { \sqrt { 2 } }$ with H to D.

4. from $\mathbb { D } \backslash [ a , 1 )$ to ${ \mathbb D } \backslash [ 0 , 1 ) ~ ( 0 < a < 1 )$ . Short solution possible using Blaschke factor

5. from $\{ z : | z | < 1 , \mathrm { R e } ( z ) > 0 \} \backslash ( 0 , 1 / 2 ]$ to H.

22. Let C and $C ^ { \prime }$ be two circles and let $z _ { 1 } \in C , z _ { 2 } \notin C , z _ { 1 } ^ { \prime } \in C ^ { \prime } , z _ { 2 } ^ { \prime } \notin C ^ { \prime }$ . Show that there is a unique fractional linear transformation f with $f ( C ) = C ^ { \prime }$ and $f ( z _ { 1 } ) = z _ { 1 } ^ { \prime } , f ( z _ { 2 } ) = z _ { 2 } ^ { \prime }$

23. Assume $f _ { n } \in H ( \Omega )$ is a sequence of holomorphic functions on the region Ω that are uniformly bounded on compact subsets and $f \in H ( \Omega )$ is such that the set $\{ z \in \Omega : \operatorname* { l i m } _ { n  \infty } f _ { n } ( z ) = f ( z ) \}$ has a limit point in Ω. Show that $f _ { n }$ converges to f uniformly on compact subsets of Ω.

24. Let $\psi _ { \alpha } ( z ) = { \frac { \alpha - z } { 1 - \bar { \alpha } z } }$ with $| \alpha | < 1$ and ${ \mathbb D } = \{ z : ~ | z | < 1 \}$ . Prove that

$$
\bullet \ \frac { 1 } { \pi } \iint _ { \mathbb { D } } | \psi _ { \alpha } ^ { \prime } | ^ { 2 } d x d y = 1 .
$$

$$
\bullet \ \frac { 1 } { \pi } \iint _ { \mathbb { D } } | \psi _ { \alpha } ^ { \prime } | d x d y = \frac { 1 - | \alpha | ^ { 2 } } { | \alpha | ^ { 2 } } \log \frac { 1 } { 1 - | \alpha | ^ { 2 } } .
$$

25. Prove that $f ( z ) = - \frac { 1 } { 2 } \left( z + \frac { 1 } { z } \right)$ is a conformal map from half disc $\left\{ z = x + i y : \ | z | < 1 , \ y > 0 \right\}$ to upper half plane $\mathbb { H } \overset { \cdot } { = } \left\{ z = \overset { \cdot } { x } + i y : \ y > 0 \right\}$

26. Let Ω be a simply connected open set and let γ be a simple closed contour in Ω and enclosing a bounded region U anticlockwise. Let $f : \Omega \longrightarrow \mathbb { C }$ be a holomorphic function and $| f ( z ) | \leq M$ for all $z \in \gamma$ . Prove that $| f ( z ) | \leq M$ for all $z \in U$

27. Compute the following integrals. (i) $\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x , 0 < a < n { \mathrm { ~ ( i i ) } } \int _ { 0 } ^ { \infty } { \frac { \log x } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x$

28. Let $0 < r < 1$ . Show that polynomials $P _ { n } ( z ) = 1 + 2 z + 3 z ^ { 2 } + \cdot \cdot \cdot + n z ^ { n - 1 }$ have no zeros in $| z | < r$ for all sufficiently large $n \mathrm { { } s . }$

29. Let f be holomorphic in a neighborhood of $D _ { r } ( z _ { 0 } )$ . Show that for any $s < r .$ , there exists a constant $c > 0$ such that

$$
\| f \| _ { ( \infty , s ) } \leq c \| f \| _ { ( 1 , r ) } ,
$$

where $\| f \| _ { ( \infty , s ) } = \operatorname* { s u p } _ { z \in D _ { s } ( z _ { 0 } ) } | f ( z ) | { \mathrm { ~ a n d ~ } } \| f \| _ { ( 1 , r ) } = \int _ { D _ { r } ( z _ { 0 } ) } | f ( z ) | d x d y .$

30. Let $\psi _ { \alpha } ( z ) = { \frac { \alpha - z } { 1 - \bar { \alpha } z } }$ with $| \alpha | < 1$ and ${ \mathbb D } = \{ z : ~ | z | < 1 \}$ . Prove that

$$
\bullet \ \frac { 1 } { \pi } \iint _ { \mathbb { D } } | \psi _ { \alpha } ^ { \prime } | ^ { 2 } d x d y = 1 .
$$

$$
\bullet \ \frac { 1 } { \pi } \iint _ { \mathbb { D } } | \psi _ { \alpha } ^ { \prime } | d x d y = \frac { 1 - | \alpha | ^ { 2 } } { | \alpha | ^ { 2 } } \log \frac { 1 } { 1 - | \alpha | ^ { 2 } } .
$$

Prove that $f ( z ) = - \frac { 1 } { 2 } \left( z + \frac { 1 } { z } \right)$ is a conformal map from half disc $\left\{ z = x + i y : \ | z | < 1 , \ y > 0 \right\}$ to upper half plane $\mathbb { H } \overset { \cdot } { = } \left\{ z = \overset { \cdot } { x } + i y : \ y > 0 \right\}$

31. Let Ω be a simply connected open set and let γ be a simple closed contour in Ω and enclosing a bounded region U anticlockwise. Let $f : \Omega \longrightarrow \mathbb { C }$ be a holomorphic function and $| f ( z ) | \leq M$ for all $z \in \gamma$ . Prove that $| f ( z ) | \leq M$ for all $z \in U$

32. Compute the following integrals. (i) $\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x , 0 < a < n$

$$
{ \mathrm { ( i i ) } } \int _ { 0 } ^ { \infty } { \frac { \log x } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x
$$

33. Let $0 < r < 1$ . Show that polynomials $P _ { n } ( z ) = 1 + 2 z + 3 z ^ { 2 } + \cdot \cdot \cdot + n z ^ { n - 1 }$ have no zeros in $| z | < r$ for all sufficiently large n’s.

34. Let f be holomorphic in a neighborhood of $D _ { r } ( z _ { 0 } )$ . Show that for any $s < r ,$ , there exists a constant $c > 0$ such that

$$
\| f \| _ { ( \infty , s ) } \leq c \| f \| _ { ( 1 , r ) } ,
$$

where $\| f \| _ { ( \infty , s ) } = \operatorname* { s u p } _ { z \in D _ { s } ( z _ { 0 } ) } | f ( z ) | { \mathrm { ~ a n d ~ } } \| f \| _ { ( 1 , r ) } = \int _ { D _ { r } ( z _ { 0 } ) } | f ( z ) | d x d y .$

## 6 Fall 2016

1. Let $u ( x , y )$ be harmonic and have continuous partial derivatives of order three in an open disc of radius $R > 0$ .

(a) Let two points $( a , b ) , ( x , y )$ in this disk be given. Show that the following integral is independent of the path in this disk joining these points:

$$
v ( x , y ) = \int _ { a , b } ^ { x , y } ( - \frac { \partial u } { \partial y } d x + \frac { \partial u } { \partial x } d y ) .
$$

(b)

(i) Prove that $u ( x , y ) + i v ( x , y )$ is an analytic function in this disc.

(ii) Prove that $v ( x , y )$ is harmonic in this disc.

2. (a) $f ( z ) = u ( x , y ) + i v ( x , y )$ be analytic in a domain $D \subset \mathbb { C }$ . Let $z _ { 0 } = ( x _ { 0 } , y _ { 0 } )$ be a point in D which is in the intersection of the curves $u ( x , y ) = c _ { 1 }$ and $v ( x , y ) = c _ { 2 }$ , where $c _ { 1 }$ and $c _ { 2 }$ are constants. Suppose that $f ^ { \prime } ( z _ { 0 } ) \neq 0$ . Prove that the lines tangent to these curves at z0 are perpendicular.

(b) Let $f ( z ) = z ^ { 2 }$ be defined in $\mathbb { C } .$

(c) Describe the level curves of $\operatorname { R e } ( f )$ and of $\operatorname { I m } ( f )$

(ii) What are the angles of intersections between the level curves $\operatorname { R e } ( f ) = 0$ and $\operatorname { I m } ( f ) ?$ Is your answer in agreement with part a) of this question?

3. (a) $f : D  \mathbb { C }$ be a continuous function, where $D \subset \mathbb { C }$ is a domain.Let $\alpha : [ a , b ] \to D$ be a smooth curve. Give a precise definition of the complex line integral

$$
\int _ { \alpha } f .
$$

(b) Assume that there exists a constant M such that $| f ( \tau ) | \le M$ for all $\tau \in { \mathrm { I m a g e } } ( \alpha )$ . Prove that

$$
\big | \int _ { \alpha } f \big | \leq M \times \mathrm { l e n g t h } ( \alpha ) .
$$

(c) Let $C _ { R }$ be the circle $| z | = R ,$ , described in the counterclockwise direction, where $R > 1$ Provide an upper bound for $| \int _ { C _ { R } } \frac { \log { ( z ) } } { z ^ { 2 } } |$ , which depends only on R and other constants.

4. (a) Let Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Assume the existence of a non-negative integer m, and of positive constants L and R, such that for all $z { \mathrm { ~ w i t h ~ } } | z | > R$ the inequality

$$
| f ( z ) | \leq L | z | ^ { m }
$$

holds. Prove that f is a polynomial of degree $\leq m$

(b) Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Suppose that there exists a real number M such that for all $z \in \mathbb { C }$

$$
\operatorname { R e } ( f ) \leq M .
$$

Prove that f must be a constant.

5. Prove that all the roots of the complex polynomial

$$
z ^ { 7 } - 5 z ^ { 3 } + 1 2 = 0
$$

lie between the circles $| z | = 1$ and $| z | = 2$

6. (a) Let F be an analytic function inside and on a simple closed curve C, except for a pole of order m $\geq 1$ at $z = a$ inside C. Prove that

$$
\frac { 1 } { 2 \pi i } \oint _ { C } F ( \tau ) d \tau = \operatorname * { l i m } _ { \tau  a } \frac { d ^ { m - 1 } } { d \tau ^ { m - 1 } } \big ( ( \tau - a ) ^ { m } F ( \tau ) \big ) \big ) .
$$

(b) Evaluate

$$
\oint _ { C } { \frac { e ^ { \tau } } { ( \tau ^ { 2 } + \pi ^ { 2 } ) ^ { 2 } } } d \tau
$$

where C is the circle $| z | = 4$

7. Find the conformal map that takes the upper half-plane comformally onto the half-strip $\{ w = x + i y : \ - \pi / 2 < x < \pi / 2 \ y > 0 \}$

8. Compute the integral $\int _ { - \infty } ^ { \infty } { \frac { e ^ { - 2 \pi i x \xi } } { \cosh \pi x } } d$ dx where cosh $z = { \frac { e ^ { z } + e ^ { - z } } { 2 } }$