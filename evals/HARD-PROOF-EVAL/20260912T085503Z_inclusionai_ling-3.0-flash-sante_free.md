# Eval: inclusionai/ling-3.0-flash-sante:free

- Run timestamp (UTC): 20260912T085503Z
- Model timestamp (UTC): 20260912T090817Z
- Model: `inclusionai/ling-3.0-flash-sante:free`
- Provider: `inclusionai`
- Success: True
- Usage: {"prompt_tokens": 3717, "completion_tokens": 22670, "total_tokens": 26387, "cost": 0, "is_byok": false, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "cost_details": {"upstream_inference_cost": 0, "upstream_inference_prompt_cost": 0, "upstream_inference_completions_cost": 0}, "completion_tokens_details": {"reasoning_tokens": 13477, "image_tokens": 0, "audio_tokens": 0}}
- Problem source: `HARD-PROOF-EVAL.md` verbatim (Koebe-Bieberbach)
- Prompt length: 8778 chars
- Max tokens: per-model saturated (32768), timeout: none

---

## Chain-of-Thought (reasoning)

We need to solve the problem completely, with full proofs for each part (a)-(g). The problem is about the Koebe-Bieberbach radius theorem for normalized univalent functions. We need to provide a rigorous solution.

Let's parse the problem carefully.

We have a holomorphic map f: D -> C with f(0)=0. By open mapping theorem, image contains a small disc centered at origin. Question: does there exist r>0 such that for all f with f(0)=0, we have D_r(0) subset f(D)?

(a) Show that with no further restrictions on f, no such r exists. It suffices to find a sequence of functions {f_n} holomorphic in D such that 1/n not in f_n(D). Compute f_n'(0), and discuss.

(b) Assume in addition that f also satisfies f'(0)=1. Show that despite this new assumption, there exists no r>0 satisfying the desired condition. Hint: Try f_epsilon(z) = epsilon(e^{z/epsilon} - 1).

The Koebe-Bieberbach theorem states that if in addition to f(0)=0 and f'(0)=1 we also assume that f is injective, then such an r exists and the best possible value is r=1/4.

(c) As a first step, show that if h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... is analytic and injective for 0<|z|<1, then sum_{n=1}^\infty n|c_n|^2 <= 1. Hint: Calculate the area of the complement of h(D_r(0) - {0}) where 0<rho<1, and let rho->1.

(d) If f(z) = z + a_2 z^2 + ... satisfies the hypotheses of the theorem, show that there exists another function g satisfying the hypotheses of the theorem such that g^2(z) = f(z^2). Hint: f(z)/z is nowhere vanishing so there exists psi such that psi^2(z) = f(z)/z and psi(0)=1. Check that g(z) = z psi(z^2) is injective.

(e) With the notation of the previous part, show that |a_2| <= 2, and that equality holds iff f(z) = z/(1 - e^{i theta} z)^2 for some theta in R. Hint: What is the power series expansion of 1/g(z)? Use part (c).

(f) If h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... is injective on D and avoids the values z_1 and z_2, show that |z_1 - z_2| <= 4. Hint: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).

(g) Complete the proof of the theorem. Hint: If f avoids w, then 1/f avoids 0 and 1/w.

We need to provide full proofs for each part. Let's do it step by step.

First, some background: D = unit disc {z in C: |z|<1}. Univalent means injective holomorphic.

Part (a): Without further restrictions, no uniform r exists.

We need to find a sequence f_n holomorphic on D, f_n(0)=0, such that 1/n not in f_n(D). Then for any r>0, choose n large enough so that 1/n < r, then 1/n is in D_r(0) but not in f_n(D), so D_r(0) not subset of f_n(D).

The simplest: f_n(z) = z/n. Then f_n(0)=0, holomorphic. f_n(D) = {z/n: |z|<1} = D_{1/n}(0). Then 1/n is not in f_n(D) because |1/n| = 1/n, but the disc is open, so points with modulus < 1/n. Actually 1/n is on the boundary, not in the open disc. So 1/n not in f_n(D). Also f_n'(0) = 1/n -> 0. So the derivative at 0 can be arbitrarily small, which is why no uniform r exists.

Alternatively, we could use f_n(z) = z/n + ... but the hint says compute f_n'(0) and discuss. So we should mention that f_n'(0) = 1/n -> 0, so the condition f'(0)=1 is necessary to prevent scaling down.

Part (b): With f'(0)=1, still no uniform r.

Hint: f_epsilon(z) = epsilon(e^{z/epsilon} - 1). Let's check: f_epsilon(0) = epsilon(1-1)=0. f_epsilon'(z) = epsilon * (1/epsilon) e^{z/epsilon} = e^{z/epsilon}. So f_epsilon'(0) = 1. Good.

Now, f_epsilon(D) = {epsilon(e^{z/epsilon} - 1): |z|<1}. Since e^{w} never equals 0, e^{z/epsilon} != 0, so f_epsilon(z) != -epsilon. Thus -epsilon is omitted. For any r>0, choose epsilon < r. Then -epsilon is in D_r(0) (since |-epsilon| = epsilon < r), but -epsilon not in f_epsilon(D). So no uniform r works.

We should also note that f_epsilon is holomorphic on D (entire). So this shows that even with f'(0)=1, the image can omit a point arbitrarily close to 0.

Part (c): Area theorem.

We have h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... analytic and injective for 0<|z|<1. We need to show sum_{n=1}^\infty n|c_n|^2 <= 1.

The hint: Calculate the area of the complement of h(D_r(0) \ {0}) where 0<rho<1, and let rho->1.

Let's denote D_r = {z: |z|<r}. Then h is injective on the punctured disc D_r \ {0}. The image is h(D_r \ {0}). Since h has a simple pole at 0, the image covers the exterior of some region. The complement of h(D_r \ {0}) in C is a compact set (since h maps the boundary |z|=r to a closed curve, and by injectivity, the image of the punctured disc is the exterior of the image of the circle, maybe with some orientation). Actually, for univalent functions on an annulus or punctured disc, the area of the complement can be computed via the area theorem.

Let's compute the area of the complement of h(D_r \ {0}). Since h is injective on 0<|z|<r, the image of the punctured disc is a domain. The complement is the set of points not hit. Because h has a simple pole at 0, near 0, h(z) ~ 1/z, so the image of a small circle |z|=epsilon is a large circle of radius ~1/epsilon. As epsilon->0, the image covers the exterior of a large disc. The complement of h(D_r \ {0}) is contained in the image of the annulus r<|z|<1? Wait, h is defined on 0<|z|<1. So for a fixed r<1, h is defined on D_r \ {0}. The complement of h(D_r \ {0}) is a compact set (since h maps the boundary |z|=r to a closed curve, and the point at infinity is in the image because of the pole). Actually, the image of D_r \ {0} is the exterior of some compact set K_r (the image of the annulus r<|z|<1? No, h is not defined outside D_r). Let's think carefully.

h is defined on the punctured unit disc. For 0<rho<1, consider the image of the punctured disc D_rho \ {0}. Since h is injective, the image is a domain. The boundary consists of the image of the circle |z|=rho and possibly the image of the puncture (which goes to infinity). Because h has a simple pole at 0, the image of a small circle around 0 is a large curve that winds around infinity. The complement of h(D_rho \ {0}) is a compact set contained in the image of the annulus rho<|z|<1? Actually, h is defined on the whole punctured unit disc, but we are only looking at the image of D_rho \ {0}. The complement of this image is the set of points w such that h(z) != w for all 0<|z|<rho. Since h is injective, the equation h(z)=w has at most one solution. For |w| large, there is a solution near 0 (because of the pole). So the complement is bounded. In fact, the complement is contained in h({rho<|z|<1})? No, h({rho<|z|<1}) is the image of the annulus, which is disjoint from h(D_rho \ {0}) by injectivity. So the complement of h(D_rho \ {0}) contains h({rho<|z|<1}) and possibly some other points? Actually, since h is injective on the whole punctured disc, the images of D_rho \ {0} and the annulus rho<|z|<1 are disjoint. The union of these two images is h(D_1 \ {0}). The complement of h(D_rho \ {0}) in C is the union of the complement of h(D_1 \ {0}) and the image of the annulus? Wait, h(D_1 \ {0}) is the image of the whole punctured disc. The complement of h(D_rho \ {0}) includes all points not hit by h on D_rho \ {0}. This includes the image of the annulus (since those points are hit only there), and also points not hit anywhere (the omitted set of h on the whole punctured disc). But h is injective, so it could omit some values. The complement of h(D_1 \ {0}) is the omitted set. So the complement of h(D_rho \ {0}) is the union of the omitted set and the image of the annulus rho<|z|<1.

But the area theorem is usually proved by computing the area of the complement of h(D_rho \ {0}) in two ways: one using the parametrization of the boundary, and one using the series expansion.

Standard proof of area theorem: For h(z) = 1/z + sum_{n=0}^\infty c_n z^n, injective on 0<|z|<1. For 0<rho<1, consider the image of the circle |z|=rho. The area of the complement of h(D_rho \ {0}) is given by pi(1/rho^2 - sum_{n=1}^\infty n|c_n|^2 rho^{2n}). Then let rho->1 to get the inequality.

Let's derive this carefully.

Let w = h(z). For z on the circle |z|=rho, we have z = rho e^{i theta}. Then h(z) = 1/(rho e^{i theta}) + sum_{n=0}^\infty c_n rho^n e^{i n theta}. The image of the circle is a closed curve (maybe self-intersecting? But since h is injective on the punctured disc, the image of the circle is a simple closed curve? Actually, h is injective on the punctured disc, so the image of the circle |z|=rho is a simple closed curve (Jordan curve) because if h(z1)=h(z2) for |z1|=|z2|=rho, then z1=z2 by injectivity. So it's a simple closed curve. The image of the punctured disc D_rho \ {0} is the exterior of this curve (since near 0, h(z) is large). So the complement of h(D_rho \ {0}) is the bounded region enclosed by this curve (including the curve itself). The area of this region can be computed using Green's theorem or the formula for area enclosed by a parametric curve.

The area enclosed by a parametric curve w(theta) = h(rho e^{i theta}) for theta from 0 to 2pi is given by (1/2) Im integral_{0}^{2pi} overline{w} w'(theta) d theta? Actually, the area of the region enclosed by a simple closed curve parameterized by w(theta) is (1/2) Im integral_0^{2pi} overline{w} dw/d theta d theta. Or equivalently, (1/2) integral_0^{2pi} (x dy - y dx). In complex notation, area = (1/2i) integral overline{w} w' d theta.

But we need the area of the complement, which is the interior of the curve. Since h is injective, the image of the punctured disc is the exterior, so the complement is the interior. The area of the interior is given by the same formula but with opposite sign? Let's check orientation. As theta increases, z = rho e^{i theta} goes counterclockwise. Near 0, h(z) ~ 1/z, so w ~ (1/rho) e^{-i theta}. As theta increases, the argument of w decreases, so the image of the circle is traversed clockwise. Thus the interior is on the right side? Let's compute carefully.

Standard area theorem: For h(z) = 1/z + sum_{n=0}^\infty c_n z^n, univalent in 0<|z|<1, the area of the complement of h(D_rho \ {0}) is pi(1/rho^2 - sum_{n=1}^\infty n|c_n|^2 rho^{2n}). Since area is nonnegative, we get the inequality.

Let's derive it.

Let w = h(z). The boundary of the complement is the image of |z|=rho. The area of the complement (the interior) is given by:

A = (1/2i) integral_{|z|=rho} overline{w} dw.

But dw = h'(z) dz. So A = (1/2i) integral_{|z|=rho} overline{h(z)} h'(z) dz.

Parameterize z = rho e^{i theta}, dz = i rho e^{i theta} d theta.

Then h(z) = 1/(rho e^{i theta}) + sum_{n=0}^\infty c_n rho^n e^{i n theta}.

overline{h(z)} = 1/(rho e^{-i theta}) + sum_{n=0}^\infty overline{c_n} rho^n e^{-i n theta}.

h'(z) = -1/z^2 + sum_{n=1}^\infty n c_n z^{n-1} = -1/(rho^2 e^{2i theta}) + sum_{n=1}^\infty n c_n rho^{n-1} e^{i (n-1) theta}.

Then overline{h(z)} h'(z) dz = [overline{h(z)} h'(z)] i rho e^{i theta} d theta.

So A = (1/2i) integral_0^{2pi} overline{h(rho e^{i theta})} h'(rho e^{i theta}) i rho e^{i theta} d theta = (rho/2) integral_0^{2pi} overline{h} h' e^{i theta} d theta.

Alternatively, use the formula A = (1/2) Im integral overline{w} dw. But let's compute directly.

Compute overline{h(z)} h'(z) dz. Since dz = i z d theta / rho? Actually z = rho e^{i theta}, so dz = i z d theta. So overline{h} h' dz = overline{h} h' i z d theta.

Thus A = (1/2i) integral_0^{2pi} overline{h} h' i z d theta = (1/2) integral_0^{2pi} overline{h} h' z d theta.

Now substitute series.

h(z) = z^{-1} + sum_{n=0}^\infty c_n z^n.
overline{h(z)} = z^{-1} (since |z|=rho, overline{z^{-1}} = overline{z}^{-1} = (rho e^{-i theta})^{-1} = rho^{-1} e^{i theta} = z/rho^2? Wait, careful: overline{z} = rho e^{-i theta} = rho^2 / z? Actually z = rho e^{i theta}, so overline{z} = rho e^{-i theta} = rho^2 / (rho e^{i theta}) = rho^2 / z. So overline{z^{-1}} = overline{z}^{-1} = (rho^2 / z)^{-1} = z / rho^2. But also z^{-1} = e^{-i theta}/rho. Its conjugate is e^{i theta}/rho = z/rho^2. Yes.

So overline{h(z)} = overline{z^{-1}} + sum_{n=0}^\infty overline{c_n} overline{z}^n = z/rho^2 + sum_{n=0}^\infty overline{c_n} (rho^2 / z)^n? Wait, overline{z}^n = (rho^2 / z)^n = rho^{2n} z^{-n}. That seems messy. Better to use the parameterization directly.

Let's use the parameterization w(theta) = h(rho e^{i theta}). Then the area enclosed by the curve w(theta) (traversed clockwise) is given by A = (1/2) integral_0^{2pi} Im( overline{w} w' ) d theta? Actually, the area of a region bounded by a simple closed curve parameterized by w(theta) is (1/2) integral_0^{2pi} (x dy - y dx) = (1/2i) integral_0^{2pi} overline{w} w' d theta. This formula gives the signed area, positive if the curve is traversed counterclockwise. Since our curve is traversed clockwise (because of the 1/z term), the signed area will be negative of the interior area. But the complement is the interior, so we take absolute value or adjust sign.

Let's compute I = integral_0^{2pi} overline{w} w' d theta.

w(theta) = rho^{-1} e^{-i theta} + sum_{n=0}^\infty c_n rho^n e^{i n theta}.
overline{w(theta)} = rho^{-1} e^{i theta} + sum_{n=0}^\infty overline{c_n} rho^n e^{-i n theta}.
w'(theta) = derivative w.r.t theta: -i rho^{-1} e^{-i theta} + sum_{n=1}^\infty i n c_n rho^n e^{i n theta}.

Now multiply overline{w} and w':

overline{w} w' = [rho^{-1} e^{i theta} + sum_{m=0}^\infty overline{c_m} rho^m e^{-i m theta}] * [-i rho^{-1} e^{-i theta} + sum_{n=1}^\infty i n c_n rho^n e^{i n theta}].

Expand:

Term 1: (rho^{-1} e^{i theta}) * (-i rho^{-1} e^{-i theta}) = -i rho^{-2}.

Term 2: (rho^{-1} e^{i theta}) * (sum_{n=1}^\infty i n c_n rho^n e^{i n theta}) = i rho^{-1} sum_{n=1}^\infty n c_n rho^n e^{i (n+1) theta}.

Term 3: (sum_{m=0}^\infty overline{c_m} rho^m e^{-i m theta}) * (-i rho^{-1} e^{-i theta}) = -i rho^{-1} sum_{m=0}^\infty overline{c_m} rho^m e^{-i (m+1) theta}.

Term 4: (sum_{m=0}^\infty overline{c_m} rho^m e^{-i m theta}) * (sum_{n=1}^\infty i n c_n rho^n e^{i n theta}) = i sum_{m=0}^\infty sum_{n=1}^\infty n overline{c_m} c_n rho^{m+n} e^{i (n-m) theta}.

Now integrate over theta from 0 to 2pi. The integral of e^{i k theta} over 0 to 2pi is 0 unless k=0, in which case it's 2pi.

Term 1: constant -i rho^{-2}. Integral = -i rho^{-2} * 2pi.

Term 2: exponent i (n+1) theta. Since n>=1, n+1 >=2, never zero. So integral = 0.

Term 3: exponent -i (m+1) theta. Since m>=0, m+1 >=1, never zero. So integral = 0.

Term 4: exponent i (n-m) theta. This is zero unless n=m. So we need n=m. But n>=1, m>=0. So m can be 0,1,2,... and n=m. So for each n>=1, m=n. Then term is i * n overline{c_n} c_n rho^{2n} e^{i 0} = i n |c_n|^2 rho^{2n}. Also m=0, n=0? But n starts at 1, so m=0 gives n=0 not allowed. So only n=m>=1.

Thus integral of term 4 = i * 2pi * sum_{n=1}^\infty n |c_n|^2 rho^{2n}.

Wait, check: term 4 is i sum_{m,n} ... e^{i(n-m)theta}. When n=m, the sum over m from 0 to infinity, n=m, but n>=1, so m>=1. So sum_{n=1}^\infty i n |c_n|^2 rho^{2n}. Then integral over theta gives 2pi times that.

So total integral I = integral_0^{2pi} overline{w} w' d theta = -i 2pi rho^{-2} + i 2pi sum_{n=1}^\infty n |c_n|^2 rho^{2n}.

Thus I = 2pi i (sum_{n=1}^\infty n |c_n|^2 rho^{2n} - rho^{-2}).

Now the area A of the complement (interior) is given by A = (1/2) |Im(I)|? Actually, the formula A = (1/2i) integral overline{w} w' d theta gives the signed area. For a clockwise curve, the signed area is negative of the geometric area. Let's compute (1/2i) I.

(1/2i) I = (1/2i) * 2pi i (sum n|c_n|^2 rho^{2n} - rho^{-2}) = pi (sum n|c_n|^2 rho^{2n} - rho^{-2}).

Since the curve is traversed clockwise, the signed area is negative of the interior area. The interior area is positive. So interior area = - (1/2i) I = pi (rho^{-2} - sum n|c_n|^2 rho^{2n}).

Thus the area of the complement of h(D_rho \ {0}) is pi (1/rho^2 - sum_{n=1}^\infty n|c_n|^2 rho^{2n}).

Since area is nonnegative, we have 1/rho^2 - sum_{n=1}^\infty n|c_n|^2 rho^{2n} >= 0, i.e., sum_{n=1}^\infty n|c_n|^2 rho^{2n} <= 1/rho^2.

Now let rho -> 1^-. By monotone convergence (or just continuity), sum_{n=1}^\infty n|c_n|^2 <= 1.

This proves part (c).

We should also note that h is injective on the punctured disc, so the image of the circle is a simple closed curve, and the area formula holds.

Part (d): Given f(z) = z + a_2 z^2 + ... injective on D, f(0)=0, f'(0)=1. Show there exists g satisfying the same hypotheses such that g^2(z) = f(z^2).

Hint: f(z)/z is nowhere vanishing. Since f is injective and f(0)=0, f(z) != 0 for z != 0. So f(z)/z != 0 for all z in D. Also f(z)/z is holomorphic on D (removable singularity at 0, with value f'(0)=1). Since D is simply connected and f(z)/z is nowhere zero, there exists a holomorphic square root psi(z) such that psi(z)^2 = f(z)/z and psi(0)=1 (choose the branch with positive value at 0). Then define g(z) = z psi(z^2). Then g(0)=0. Compute g'(0): g(z) = z (1 + (a_2/2) z^2 + ...)? Let's compute: f(z)/z = 1 + a_2 z + a_3 z^2 + ... . The square root psi(z) = 1 + (a_2/2) z + ... . Then psi(z^2) = 1 + (a_2/2) z^2 + ... . So g(z) = z + (a_2/2) z^3 + ... . So g'(0)=1. Also g is injective? Need to check.

Hint says check that g is injective. Let's verify: Suppose g(z1) = g(z2). Then z1 psi(z1^2) = z2 psi(z2^2). Square both sides: z1^2 psi(z1^2)^2 = z2^2 psi(z2^2)^2. But psi(z^2)^2 = f(z^2)/z^2. So z1^2 * f(z1^2)/z1^2 = z2^2 * f(z2^2)/z2^2, so f(z1^2) = f(z2^2). Since f is injective, z1^2 = z2^2. So z2 = +/- z1. If z2 = z1, done. If z2 = -z1, then g(z2) = g(-z1) = -z1 psi((-z1)^2) = -z1 psi(z1^2) = -g(z1). So g(z1) = g(-z1) implies g(z1) = -g(z1), so 2g(z1)=0, so g(z1)=0. But g(z)=0 only at z=0 (since g(z)/z = psi(z^2) != 0). So z1=0, thus z2=0. So g is injective.

Thus g satisfies the hypotheses: g(0)=0, g'(0)=1, g injective holomorphic on D. And g^2(z) = z^2 psi(z^2)^2 = z^2 * f(z^2)/z^2 = f(z^2). Good.

Part (e): Show |a_2| <= 2, equality iff f(z) = z/(1 - e^{i theta} z)^2.

From part (d), we have g with g^2(z) = f(z^2). Also g(z) = z + b_2 z^3 + ... (odd function). Actually, g is odd? Let's check: g(-z) = -z psi((-z)^2) = -z psi(z^2) = -g(z). So g is odd. So its power series has only odd powers: g(z) = z + b_3 z^3 + b_5 z^5 + ... . But the hint says g(z) = z psi(z^2) and psi(z) = 1 + (a_2/2) z + ... . So psi(z^2) = 1 + (a_2/2) z^2 + ... . Thus g(z) = z + (a_2/2) z^3 + ... . So the coefficient of z^3 is a_2/2.

Now consider 1/g(z). Since g has a simple zero at 0, 1/g has a simple pole at 0. Write 1/g(z) = 1/z + d_0 + d_1 z + d_2 z^2 + ... . Since g is odd, 1/g is odd? Let's check: g(-z) = -g(z), so 1/g(-z) = -1/g(z). So 1/g is odd. Thus its Laurent expansion has only odd powers: 1/g(z) = 1/z + d_1 z + d_3 z^3 + ... . So d_0 = 0, d_2 = 0, etc. In particular, the coefficient of z^1 is d_1.

Now apply part (c) to h(z) = 1/g(z). Is h injective on 0<|z|<1? Since g is injective on D and g(0)=0, g maps D onto some domain. The function 1/g is defined on D \ {0}. Is it injective? If 1/g(z1) = 1/g(z2), then g(z1) = g(z2), so z1 = z2 by injectivity of g. So yes, 1/g is injective on D \ {0}. It has a simple pole at 0. So we can apply part (c) to h = 1/g.

Part (c) says sum_{n=1}^\infty n |c_n|^2 <= 1, where c_n are the coefficients of h(z) = 1/z + c_0 + c_1 z + ... . For h = 1/g, we have c_0 = 0, c_1 = d_1, c_2 = 0, etc. So the sum is 1*|c_1|^2 + 2*|c_2|^2 + ... = |c_1|^2 + ... <= 1. Thus |c_1| <= 1.

Now we need to relate c_1 to a_2. We have g(z) = z + (a_2/2) z^3 + ... . Compute 1/g(z). Write g(z) = z (1 + (a_2/2) z^2 + ...). Then 1/g(z) = (1/z) * 1/(1 + (a_2/2) z^2 + ...) = (1/z) * (1 - (a_2/2) z^2 + ...) = 1/z - (a_2/2) z + ... . So c_1 = -a_2/2. Thus |a_2/2| <= 1, so |a_2| <= 2.

Equality |a_2| = 2 means |c_1| = 1. In part (c), equality in the area theorem sum n|c_n|^2 <= 1 occurs only when h(z) = 1/z + c_1 z (i.e., all other c_n = 0). Actually, the area theorem says the area of the complement is pi(1/rho^2 - sum n|c_n|^2 rho^{2n}). If sum n|c_n|^2 = 1, then the area of the complement is pi(1/rho^2 - rho^2) (since only n=1 term). As rho->1, the area tends to 0. This means the complement has area 0, so the image of the punctured disc is dense in C? Actually, the complement is the interior of the image of the circle. If the area is zero, the image of the circle must be a curve that encloses zero area? Wait, the area of the complement is the area of the bounded component of the complement of the image of the circle. If that area is zero, the curve must be degenerate? Actually, the equality case in the area theorem corresponds to the Koebe function or rotations. For h(z) = 1/z + c_1 z, the image of the punctured disc is the complement of a line segment? Let's recall: The Koebe function is k(z) = z/(1-z)^2 = 1/z + 2z + ...? Actually, the standard Koebe function is f(z) = z/(1-z)^2 = sum_{n=1}^\infty n z^n. Its inverse is h(w) = ...? Wait, the Koebe function maps D onto C minus a ray (-infty, -1/4]. The inverse function has a simple pole at infinity? Let's recall: The Koebe function is f(z) = z/(1-z)^2. Then f'(0)=1. It omits the value -1/4. The inverse function h(w) = ...? Actually, the inverse of the Koebe function is h(w) = (sqrt(1+w} - 1)/w? Something like that. But the standard form for the inverse of a univalent function with simple pole at infinity is h(w) = 1/w + c_1 w + ...? Wait, the Koebe function maps D onto the complement of a ray. The inverse function is defined on C \ (-infty, -1/4] and has a simple pole at infinity? Actually, the Koebe function is univalent on D, but its inverse is defined on the complement of the omitted ray. The omitted ray is (-infty, -1/4]. The inverse function h(w) maps C \ (-infty, -1/4] back to D. But h(w) has a simple pole at w=0? No, f(0)=0, so h(0)=0. The inverse function is holomorphic near 0. But the function h(z) = 1/f(1/z) maybe? Let's recall the standard area theorem: For a univalent function f(z) = z + a_2 z^2 + ... on D, the inverse function near infinity is h(w) = 1/w + a_2 + a_3/w + ...? Actually, if f is univalent on D, then f(1/z) is univalent near infinity. Define g(w) = 1/f(1/w). Then g(w) = 1/( (1/w) + a_2 (1/w)^2 + ... ) = w / (1 + a_2/w + ...) = w (1 - a_2/w + ...) = w - a_2 + ... . That's not a simple pole. Hmm.

Wait, the standard area theorem is for functions h(z) = z + b_0 + b_1/z + ... that are univalent on |z|>1. But here we have h(z) = 1/z + c_0 + c_1 z + ... univalent on 0<|z|<1. This is the same as a function univalent near infinity after inversion? Let's map: Let w = 1/z. Then h(z) = w + c_0 + c_1/w + c_2/w^2 + ... . So H(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + ... . This is univalent for |w|>1. The area theorem for such functions says sum n |c_n|^2 <= 1? Actually, the standard area theorem for H(w) = w + b_0 + sum_{n=1}^\infty b_n / w^n univalent on |w|>1 says sum n |b_n|^2 <= 1. Here b_n = c_n. So indeed sum n|c_n|^2 <= 1. The equality case is H(w) = w + c_1 / w (i.e., c_n=0 for n!=1). This corresponds to h(z) = 1/z + c_1 z. This maps the punctured disc onto the complement of a line segment (or a ray?). Actually, h(z) = 1/z + c_1 z. If |c_1|=1, this is a rotation of the Koebe function's inverse? Let's check: The Koebe function f(z) = z/(1-z)^2 maps D onto C \ (-infty, -1/4]. Its inverse function is h(w) = (sqrt{1+w}-1)/w? Let's compute: w = z/(1-z)^2. Solve for z: w(1 - 2z + z^2) = z => w - 2wz + w z^2 - z = 0 => w z^2 - (2w+1)z + w = 0. Using quadratic formula: z = [(2w+1) +/- sqrt((2w+1)^2 - 4w^2)]/(2w) = [(2w+1) +/- sqrt(4w+1)]/(2w). The branch that gives z=0 at w=0 is z = [(2w+1) - sqrt(1+4w)]/(2w). Expand sqrt(1+4w) = 1 + 2w - 2w^2 + ... . Then numerator = 2w+1 - (1+2w - 2w^2 + ...) = 2w^2 - ... . Divide by 2w gives w - ... . So near 0, h(w) = w + ... . That's not of the form 1/z + ... . So maybe the equality case corresponds to a different function.

Wait, the function h(z) = 1/z + c_1 z with |c_1|=1 maps the punctured disc onto the complement of a line segment. Let's compute: h(z) = 1/z + c_1 z. Let c_1 = e^{i alpha}. Then h(z) = (1 + c_1 z^2)/z. The image of the unit circle |z|=1 is w = e^{-i theta} + c_1 e^{i theta} = e^{-i theta} + e^{i(alpha+theta)}. This is an ellipse? Actually, as theta varies, w traces a curve. The complement of the image of the punctured disc is the image of the annulus 1<|z|<infty? No, h is defined on |z|<1. The image of |z|=r is a curve. As r->1, the curve approaches the boundary of the image of the punctured disc. The complement of the image of the punctured disc is the union of the image of the annulus 1<|z|<infty? No, h is only defined for |z|<1. The complement of h(D \ {0}) is a compact set. For h(z) = 1/z + c_1 z, the complement is a line segment. Indeed, the Koebe function's inverse has a simple pole at infinity? Let's check the standard Koebe function: f(z) = z/(1-z)^2. Its inverse g(w) satisfies g(w) = ...? Actually, the Koebe function maps D onto C \ (-infty, -1/4]. The inverse function is defined on C \ (-infty, -1/4] and maps to D. Near infinity, g(w) ~ 1/w? Let's see: f(z) ~ z for small z. For large w, f(z) = w implies z ~ w? No, f(z) = z/(1-z)^2. For large w, z is near 1? Actually, f(z) has a pole at z=1. The image of D is C \ (-infty, -1/4]. So the complement is a ray. The inverse function g(w) maps C \ (-infty, -1/4] to D. Near w=infty, g(w) ~ 1/w? Let's compute: w = z/(1-z)^2. For large w, z is near 1? Let's solve for z near 1: let z = 1 - u, small u. Then w = (1-u)/u^2 ~ 1/u^2. So u ~ 1/sqrt{w}. Then z = 1 - 1/sqrt{w} + ... . So g(w) = 1 - 1/sqrt{w} + ... . That's not a simple pole.

Wait, the area theorem is usually stated for functions of the form f(z) = z + b_0 + sum_{n=1}^\infty b_n / z^n univalent on |z|>1. The complement of the image of |z|>1 is a compact set containing infinity? Actually, the image of |z|>1 is the exterior of some compact set. The area of the complement (the bounded component) is pi(sum n|b_n|^2). Wait, the standard area theorem says: If f(z) = z + b_0 + sum_{n=1}^\infty b_n / z^n is univalent for |z|>1, then sum_{n=1}^\infty n |b_n|^2 <= 1. The complement of f({|z|>1}) has area pi(1 - sum n|b_n|^2). So equality holds when the complement has area zero, i.e., f maps onto the complement of a line segment (or a point?). Actually, the complement is a set of area zero, which must be a line segment (or a point). The extremal functions are rotations of the Koebe function: f(z) = z/(1 - e^{i theta}/z)^2? Let's check: The Koebe function is k(z) = z/(1-z)^2. Its inverse is h(w) = ...? Actually, the Koebe function maps D onto C \ (-infty, -1/4]. The function that maps the exterior of the unit disc onto the complement of a line segment is something like z + 1/z? No, Joukowsky map maps exterior of unit disc to complement of [-2,2]. But the Koebe function is different.

Let's recall: The Koebe function is f(z) = z/(1-z)^2 = sum_{n=1}^\infty n z^n. It maps D onto C \ (-infty, -1/4]. The inverse function g(w) is defined on C \ (-infty, -1/4] and satisfies g(w) = w - 2 + 3/w - ...? Let's compute: w = z/(1-z)^2. Solve for z: z = w/(1+w)^2? No, that's the inverse of something else. Actually, the inverse of the Koebe function is g(w) = (sqrt{1+w} - 1)/w? Let's check: If z = (sqrt{1+w} - 1)/w, then compute z/(1-z)^2. Let's do it: Let s = sqrt{1+w}. Then z = (s-1)/w = (s-1)/(s^2-1) = 1/(s+1). Then 1-z = 1 - 1/(s+1) = s/(s+1). So (1-z)^2 = s^2/(s+1)^2 = (1+w)/(s+1)^2. Then z/(1-z)^2 = [1/(s+1)] / [(1+w)/(s+1)^2] = (s+1)/(1+w) = (s+1)/s^2 = 1/s^2 + 1/s = 1/(1+w) + 1/sqrt{1+w}. That's not w. So that's not the inverse.

Actually, the inverse of the Koebe function is g(w) = w/(1+sqrt{1-w})^2? Something like that. Let's not get bogged down. The equality case in the area theorem for h(z) = 1/z + c_1 z corresponds to the complement being a line segment. The function h(z) = 1/z + c_1 z maps the punctured disc onto the complement of a line segment. The corresponding f is the Koebe function.

Specifically, if 1/g(z) = 1/z + c_1 z, then g(z) = z/(1 + c_1 z^2). Then f(z^2) = g(z)^2 = z^2/(1 + c_1 z^2)^2. So f(w) = w/(1 + c_1 w)^2. Let e^{i theta} = -c_1? Actually, we want f(z) = z/(1 - e^{i theta} z)^2. Let's check: If f(z) = z/(1 - a z)^2 with |a|=1, then f(z^2) = z^2/(1 - a z^2)^2. Then g(z)^2 = z^2/(1 - a z^2)^2, so g(z) = +/- z/(1 - a z^2). But g must satisfy g(0)=0, g'(0)=1. Let's compute g(z) = z/(1 - a z^2). Then g'(0)=1. And g is odd? g(-z) = -z/(1 - a z^2) = -g(z). Yes. Then 1/g(z) = (1 - a z^2)/z = 1/z - a z. So c_1 = -a. Since |a|=1, |c_1|=1. So equality holds. Conversely, if |c_1|=1, then 1/g(z) = 1/z + c_1 z, so g(z) = z/(1 + c_1 z^2). Then f(z) = g(sqrt{z})^2? Actually, f(z^2) = g(z)^2 = z^2/(1 + c_1 z^2)^2. So f(w) = w/(1 + c_1 w)^2. Let e^{i theta} = -c_1. Then f(w) = w/(1 - e^{i theta} w)^2. So equality holds iff f is a rotation of the Koebe function.

Thus part (e) is proved.

Part (f): If h(z) = 1/z + c_0 + c_1 z + ... is injective on D and avoids values z_1 and z_2, show |z_1 - z_2| <= 4.

Hint: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).

Let's define h_j(z) = 1/(h(z) - z_j). Since h avoids z_j, h(z) - z_j != 0. Also h has a simple pole at 0, so h(z) - z_j has a simple pole at 0. Thus h_j has a simple zero at 0? Wait, h(z) ~ 1/z near 0, so h(z) - z_j ~ 1/z. Then 1/(h(z) - z_j) ~ z. So h_j has a simple zero at 0, not a pole. But the hint says 1/(h(z) - z_j) is injective and has expansion 1/z + c_0 + ...? That seems contradictory. Let's check.

If h(z) = 1/z + c_0 + c_1 z + ... , then h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . Then 1/(h(z) - z_j) = 1 / (1/z + ... ) = z / (1 + (c_0 - z_j) z + ... ) = z (1 - (c_0 - z_j) z + ... ) = z - (c_0 - z_j) z^2 + ... . So it has a simple zero at 0, not a simple pole. So the hint "1/(h(z) - z_j) is injective and has expansion 1/z + c_0 + ..." seems wrong? Wait, maybe the hint means something else. Let's read the hint: "Look at the second coefficient in the power series expansion of 1/(h(z) - z_j)." But if h avoids z_j, then h(z) - z_j is never zero. However, h has a pole at 0, so h(z) - z_j has a pole at 0. Then 1/(h(z) - z_j) has a zero at 0. So its expansion starts with z, not 1/z. So the hint might be miswritten? Or perhaps they consider h(z) - z_j and then take reciprocal? Let's think.

Alternatively, maybe they define a new function H(z) = 1/(h(z) - z_j). Since h is injective, H is also injective? If h(z1) != h(z2), then h(z1) - z_j != h(z2) - z_j, so 1/(h(z1)-z_j) != 1/(h(z2)-z_j). So yes, H is injective. H has a zero at 0. But we can consider the function k(z) = 1/H(z) = h(z) - z_j. That has a simple pole at 0. But the hint says "1/(h(z) - z_j) is injective and has expansion 1/z + c_0 + ...". That would be true if h(z) - z_j had a zero at 0, but it has a pole. So maybe the hint is for a different function? Let's re-read the problem statement for (f):

"(f) If h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... is injective on D and avoids the values z_1 and z_2, show that |z_1 - z_2| <= 4. [Hint: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).]"

Wait, maybe they mean the function h(z) - z_j avoids 0, so we can consider its reciprocal? But the reciprocal has a zero at 0. However, we can apply a transformation to get a function with a simple pole. For example, consider the function p(z) = 1/(h(z) - z_j) - z_j? No.

Alternatively, maybe the hint is to consider the function H(z) = 1/(h(z) - z_j). Since h avoids z_j, H is holomorphic and injective on D. H(0) = 0 (since h has a pole). So H(z) = z + d_2 z^2 + ... (after scaling? Actually H'(0) = ? Let's compute: h(z) = 1/z + c_0 + c_1 z + ... . Then h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . Then 1/(h(z) - z_j) = z / (1 + (c_0 - z_j) z + c_1 z^2 + ... ) = z (1 - (c_0 - z_j) z + ... ) = z - (c_0 - z_j) z^2 + ... . So H(z) = z + d_2 z^2 + ... with d_2 = -(c_0 - z_j). But H is injective and H(0)=0, H'(0)=1. So H is normalized univalent. Then we can apply the result of part (e) to H? But H is not of the form 1/z + ... . However, we can consider the inverse function? Or we can apply the area theorem to H? No, H is holomorphic on D, not on a punctured disc.

Wait, maybe the hint is to consider the function 1/(h(z) - z_j) and then apply part (c) to it after a change of variable? But part (c) requires a simple pole at 0. H has a simple zero at 0. So we can consider the function 1/H(z) = h(z) - z_j, which has a simple pole at 0. But 1/H is not injective? Actually, if H is injective, then 1/H is also injective (since w -> 1/w is injective on C\{0}). But 1/H = h - z_j has a simple pole at 0. So we can apply part (c) to 1/H? Let's check: 1/H(z) = h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . This is of the form 1/z + C_0 + C_1 z + ... . And it's injective on 0<|z|<1 (since h is injective and subtracting z_j doesn't change injectivity). So we can apply part (c) to this function. Then the coefficient c_1 in part (c) for this function is c_1 (the same as in h). But we need to relate z_1 and z_2.

Alternatively, consider the function H_j(z) = 1/(h(z) - z_j). This is injective and holomorphic on D, with H_j(0)=0, H_j'(0)=1. So H_j is normalized univalent. Then by part (e), the coefficient of z^2 in H_j is bounded by 2 in absolute value. The coefficient of z^2 in H_j is -(c_0 - z_j) = z_j - c_0. So |z_j - c_0| <= 2? Wait, H_j(z) = z + d_2 z^2 + ... . Then by part (e), |d_2| <= 2. But d_2 = -(c_0 - z_j) = z_j - c_0. So |z_j - c_0| <= 2 for each j=1,2. Then by triangle inequality, |z_1 - z_2| <= |z_1 - c_0| + |z_2 - c_0| <= 2 + 2 = 4. That gives the result! And the hint says "Look at the second coefficient in the power series expansion of 1/(h(z) - z_j)." Indeed, the second coefficient (coefficient of z^2? Or coefficient of z^1? Wait, H_j(z) = 1/(h(z) - z_j) = z + (z_j - c_0) z^2 + ... . The second coefficient is the coefficient of z^2, which is z_j - c_0. So the hint is exactly that.

But wait, part (e) applies to functions f(z) = z + a_2 z^2 + ... injective. Here H_j(z) = 1/(h(z) - z_j) is injective? Let's verify: h is injective, so h(z1) != h(z2) for z1 != z2. Then h(z1) - z_j != h(z2) - z_j. Since the map w -> 1/w is injective on C \ {0}, we have 1/(h(z1) - z_j) != 1/(h(z2) - z_j). So H_j is injective. Also H_j is holomorphic on D because h(z) - z_j != 0 for all z in D (since h avoids z_j). And H_j(0) = 0 because h has a pole at 0, so h(z) - z_j ~ 1/z, so 1/(h(z)-z_j) ~ z. More precisely, H_j(z) = z - (c_0 - z_j) z^2 + ... . So H_j'(0) = 1. Thus H_j satisfies the hypotheses of the theorem (normalized univalent). Then by part (e), the second coefficient a_2(H_j) satisfies |a_2(H_j)| <= 2. But a_2(H_j) = z_j - c_0. So |z_j - c_0| <= 2. Then |z_1 - z_2| <= |z_1 - c_0| + |c_0 - z_2| <= 4.

Thus part (f) is proved.

But we need to be careful: part (e) says |a_2| <= 2 for any normalized univalent function. So we can apply it to H_j. However, H_j is defined on D and is injective. So yes.

Alternatively, we could apply part (c) directly to h(z) - z_j? But h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . This is of the form required in (c). Then the coefficient c_1 in (c) is c_1 (the same for both j). That doesn't give a relation between z_1 and z_2. So the hint about 1/(h(z) - z_j) is the right approach.

Wait, the hint says "Look at the second coefficient in the power series expansion of 1/(h(z) - z_j)." That matches our H_j. The second coefficient is the coefficient of z^2? Or coefficient of z^1? Usually "second coefficient" might mean the coefficient of z^1 (the linear term) or z^2? In the expansion H_j(z) = z + a_2 z^2 + ..., the second coefficient is a_2. So that's consistent.

Thus part (f) is done.

Part (g): Complete the proof of the theorem.

We need to show that for f injective, f(0)=0, f'(0)=1, we have D_{1/4}(0) subset f(D). The hint: If f avoids w, then 1/f avoids 0 and 1/w.

Suppose there exists w with |w| < 1/4 such that w not in f(D). Consider the function h(z) = 1/f(z). Since f is injective and f(0)=0, f(z) != 0 for z != 0. So h is defined and holomorphic on D \ {0}. Near 0, f(z) ~ z, so h(z) ~ 1/z. So h has a simple pole at 0. Also h is injective on D \ {0} (since f is injective and nonzero away from 0). So h satisfies the hypotheses of part (c) and (f). Moreover, h avoids 0 (since f(z) is finite and nonzero for z != 0, so 1/f(z) != 0). And h avoids 1/w (since f avoids w). So h avoids 0 and 1/w. Then by part (f), |0 - 1/w| <= 4, i.e., 1/|w| <= 4, so |w| >= 1/4. Contradiction. Therefore no such w exists, so D_{1/4}(0) subset f(D).

We also need to show that 1/4 is best possible, i.e., there exists a function for which the image omits a point at distance exactly 1/4 from the origin. The Koebe function f(z) = z/(1-z)^2 is such an example. It omits the value -1/4. Let's verify: f(z) = z/(1-z)^2. For z in D, does it omit -1/4? Solve z/(1-z)^2 = -1/4 => 4z = -(1-z)^2 = -(1 - 2z + z^2) = -1 + 2z - z^2 => z^2 + 2z + 1 = 0 => (z+1)^2 = 0 => z = -1. But z = -1 is on the boundary, not in D. So -1/4 is omitted. And |-1/4| = 1/4. So the radius 1/4 is sharp.

Thus the theorem is proved.

Now we need to write a complete solution with full proofs for each part (a)-(g). We should be careful to include all details, justifications, and reasoning.

Let's structure the solution:

- Introduction: Define D, state the problem.

- Part (a): Provide the sequence f_n(z) = z/n. Show f_n(0)=0, holomorphic. Show 1/n not in f_n(D). Compute f_n'(0) = 1/n -> 0. Conclude no uniform r exists.

- Part (b): Provide f_epsilon(z) = epsilon(e^{z/epsilon} - 1). Show f_epsilon(0)=0, f_epsilon'(0)=1. Show f_epsilon(D) omits -epsilon. Conclude no uniform r exists.

- Part (c): State the area theorem. Compute the area of the complement of h(D_rho \ {0}) using the parametric formula. Derive the inequality sum n|c_n|^2 <= 1.

- Part (d): Construct psi as holomorphic square root of f(z)/z. Define g(z) = z psi(z^2). Show g(0)=0, g'(0)=1, g injective, and g^2(z) = f(z^2).

- Part (e): Use g from (d). Note g is odd, so 1/g has expansion 1/z + c_1 z + ... . Apply (c) to 1/g to get |c_1| <= 1. Relate c_1 to a_2: c_1 = -a_2/2. Thus |a_2| <= 2. Equality case: forces 1/g(z) = 1/z + e^{i theta} z, leading to g(z) = z/(1 + e^{i theta} z^2), and f(z) = z/(1 - e^{i theta} z)^2 (adjusting theta).

- Part (f): For h avoiding z_1, z_2, define H_j(z) = 1/(h(z) - z_j). Show H_j is normalized univalent. Its second coefficient is z_j - c_0. By part (e), |z_j - c_0| <= 2. Then triangle inequality gives |z_1 - z_2| <= 4.

- Part (g): Suppose f avoids w with |w| < 1/4. Then h = 1/f avoids 0 and 1/w. Apply (f) to h: |0 - 1/w| <= 4 => |w| >= 1/4, contradiction. Hence D_{1/4}(0) subset f(D). Show sharpness with Koebe function.

We need to ensure all steps are rigorous. Let's write out the details.

Part (a) details:

Define f_n(z) = z/n for n >= 1. Then f_n is holomorphic on D, f_n(0) = 0. The image f_n(D) = {z/n : |z| < 1} = D_{1/n}(0). The point 1/n has modulus 1/n, so it lies on the boundary of f_n(D), not in the open disc. Thus 1/n not in f_n(D). However, 1/n is in D_r(0) for any r > 1/n. So for any candidate r > 0, choose n > 1/r. Then 1/n < r, so 1/n in D_r(0), but 1/n not in f_n(D). Hence D_r(0) not subset of f_n(D). Therefore no such r exists.

Compute f_n'(0) = 1/n. As n -> infinity, f_n'(0) -> 0. This shows that the condition f'(0) = 1 is essential to prevent the derivative from shrinking, which would allow the image to be arbitrarily small near the origin.

Part (b) details:

Define f_epsilon(z) = epsilon(e^{z/epsilon} - 1) for epsilon > 0. Then f_epsilon(0) = epsilon(1-1) = 0. f_epsilon'(z) = epsilon * (1/epsilon) e^{z/epsilon} = e^{z/epsilon}. So f_epsilon'(0) = 1. The function is entire, hence holomorphic on D. Since e^{z/epsilon} never equals 0, f_epsilon(z) = -epsilon has no solution. Thus -epsilon not in f_epsilon(D). For any r > 0, choose epsilon < r. Then -epsilon is in D_r(0) (since |-epsilon| = epsilon < r), but -epsilon not in f_epsilon(D). Hence no uniform r works.

Note: The hint suggests this function. It's important to verify that f_epsilon is indeed holomorphic and satisfies the conditions.

Part (c) details:

Let h(z) = 1/z + sum_{n=0}^\infty c_n z^n, analytic and injective for 0 < |z| < 1. For 0 < rho < 1, consider the image of the punctured disc D_rho^* = {z: 0 < |z| < rho}. Since h is injective, the image h(D_rho^*) is a domain. The boundary of this domain includes the image of the circle |z| = rho. Because h has a simple pole at 0, the image of a small circle around 0 is a large curve that encloses the complement. The complement of h(D_rho^*) in C is a compact set K_rho (the bounded component of the complement). The area of K_rho can be computed using the formula for the area enclosed by a parametric curve.

The curve is gamma_rho(theta) = h(rho e^{i theta}) for theta in [0, 2pi]. Since h is injective, gamma_rho is a simple closed curve. The orientation is clockwise because h(z) ~ 1/z near 0. The area of the interior (which is K_rho) is given by

Area(K_rho) = (1/2) |Im integral_0^{2pi} overline{gamma_rho} gamma_rho' d theta|.

But we can compute the signed area:

A_signed = (1/2i) integral_0^{2pi} overline{gamma_rho} gamma_rho' d theta.

Since the curve is clockwise, A_signed = -Area(K_rho).

Compute the integral:

gamma_rho(theta) = rho^{-1} e^{-i theta} + sum_{n=0}^\infty c_n rho^n e^{i n theta}.
gamma_rho'(theta) = -i rho^{-1} e^{-i theta} + sum_{n=1}^\infty i n c_n rho^n e^{i n theta}.

Then overline{gamma_rho} gamma_rho' = [rho^{-1} e^{i theta} + sum_{m=0}^\infty overline{c_m} rho^m e^{-i m theta}] * [-i rho^{-1} e^{-i theta} + sum_{n=1}^\infty i n c_n rho^n e^{i n theta}].

Multiplying and integrating term by term, only the constant terms survive. The constant term from the product of the first terms is -i rho^{-2}. The constant term from the product of the series terms occurs when n = m, giving i n |c_n|^2 rho^{2n}. There are no cross terms that give constant exponent because the exponents are (n+1) and -(m+1), which are never zero for n>=1, m>=0. Thus

integral_0^{2pi} overline{gamma_rho} gamma_rho' d theta = 2pi (-i rho^{-2}) + 2pi i sum_{n=1}^\infty n |c_n|^2 rho^{2n} = 2pi i (sum_{n=1}^\infty n |c_n|^2 rho^{2n} - rho^{-2}).

Therefore

A_signed = (1/2i) * 2pi i (sum n|c_n|^2 rho^{2n} - rho^{-2}) = pi (sum n|c_n|^2 rho^{2n} - rho^{-2}).

Since the curve is clockwise, Area(K_rho) = -A_signed = pi (rho^{-2} - sum_{n=1}^\infty n |c_n|^2 rho^{2n}).

Since Area(K_rho) >= 0, we have sum_{n=1}^\infty n |c_n|^2 rho^{2n} <= rho^{-2} for all rho in (0,1). Letting rho -> 1^- gives sum_{n=1}^\infty n |c_n|^2 <= 1.

This completes part (c).

Part (d) details:

Given f(z) = z + a_2 z^2 + ... injective on D. Since f is injective and f(0)=0, f(z) != 0 for z != 0. Thus f(z)/z != 0 for all z in D. Also f(z)/z is holomorphic on D (removable singularity at 0, with value f'(0)=1). Since D is simply connected and f(z)/z is nowhere zero, there exists a holomorphic function psi on D such that psi(z)^2 = f(z)/z. We choose the branch with psi(0) = 1 (since f(z)/z -> 1 as z->0). Define g(z) = z psi(z^2). Then g(0) = 0. Compute g'(z): g'(z) = psi(z^2) + z * psi'(z^2) * 2z. At z=0, g'(0) = psi(0) = 1. So g'(0)=1.

Check injectivity: Suppose g(z1) = g(z2). Then z1 psi(z1^2) = z2 psi(z2^2). Squaring both sides: z1^2 psi(z1^2)^2 = z2^2 psi(z2^2)^2. But psi(z^2)^2 = f(z^2)/z^2. So z1^2 * f(z1^2)/z1^2 = z2^2 * f(z2^2)/z2^2, giving f(z1^2) = f(z2^2). Since f is injective, z1^2 = z2^2. Thus z2 = epsilon z1 with epsilon = +/- 1. If epsilon = 1, done. If epsilon = -1, then z2 = -z1. Then g(z2) = g(-z1) = -z1 psi((-z1)^2) = -z1 psi(z1^2) = -g(z1). Since g(z1) = g(z2) = -g(z1), we get 2g(z1) = 0, so g(z1) = 0. But g(z) = 0 implies z psi(z^2) = 0, so z=0 (since psi(z^2) = sqrt{f(z^2)/z^2} != 0 for z != 0). Thus z1 = 0, so z2 = 0. Hence g is injective.

Finally, g^2(z) = z^2 psi(z^2)^2 = z^2 * f(z^2)/z^2 = f(z^2). So g satisfies the hypotheses and g^2(z) = f(z^2).

Part (e) details:

From part (d), g is odd: g(-z) = -z psi((-z)^2) = -z psi(z^2) = -g(z). So g(z) = z + b_3 z^3 + b_5 z^5 + ... . The relation f(z^2) = g(z)^2 gives:

f(z^2) = z^2 + a_2 z^4 + a_3 z^6 + ... = (z + b_3 z^3 + ...)^2 = z^2 + 2 b_3 z^4 + ... . Comparing coefficients of z^4: a_2 = 2 b_3. So b_3 = a_2/2.

Now consider h(z) = 1/g(z). Since g is injective and g(0)=0, g(z) != 0 for z != 0. Thus h is holomorphic and injective on D \ {0}. It has a simple pole at 0: h(z) = 1/z + d_0 + d_1 z + ... . Since g is odd, h is odd: h(-z) = 1/g(-z) = -1/g(z) = -h(z). Thus the Laurent expansion of h has only odd powers: h(z) = 1/z + d_1 z + d_3 z^3 + ... . So d_0 = 0, d_2 = 0, etc.

Apply part (c) to h. The coefficients are c_0 = d_0 = 0, c_1 = d_1, c_2 = 0, ... . Then sum_{n=1}^\infty n |c_n|^2 = |d_1|^2 + 3|d_3|^2 + ... <= 1. In particular, |d_1| <= 1.

Now compute d_1 from g. Since g(z) = z (1 + (a_2/2) z^2 + ... ), we have

1/g(z) = (1/z) * (1 + (a_2/2) z^2 + ... )^{-1} = (1/z) * (1 - (a_2/2) z^2 + ... ) = 1/z - (a_2/2) z + ... .

Thus d_1 = -a_2/2. Therefore |a_2/2| <= 1, so |a_2| <= 2.

Equality |a_2| = 2 implies |d_1| = 1. Then the sum in part (c) is >= |d_1|^2 = 1, so equality holds throughout: all other c_n = 0. Thus h(z) = 1/z + d_1 z with |d_1| = 1. Write d_1 = -e^{i theta} (or e^{i theta} depending on sign). Then 1/g(z) = 1/z - e^{i theta} z (absorbing sign into theta). Solving for g: g(z) = z/(1 + e^{i theta} z^2). Then f(z^2) = g(z)^2 = z^2/(1 + e^{i theta} z^2)^2. Replacing z^2 by z, we get f(z) = z/(1 + e^{i theta} z)^2. Letting e^{i phi} = -e^{i theta}, we can write f(z) = z/(1 - e^{i phi} z)^2. Conversely, for any such f, one checks that |a_2| = 2 (since a_2 = 2 e^{i theta} for f(z) = z/(1 - e^{i theta} z)^2). This completes part (e).

Part (f) details:

Let h(z) = 1/z + c_0 + c_1 z + ... be injective on D and avoid z_1 and z_2. For each j = 1,2, define

H_j(z) = 1/(h(z) - z_j).

Since h avoids z_j, the denominator never vanishes. Since h has a simple pole at 0, h(z) - z_j has a simple pole at 0, so H_j has a simple zero at 0. Moreover, H_j is injective: if H_j(z1) = H_j(z2), then h(z1) - z_j = h(z2) - z_j, so h(z1) = h(z2), so z1 = z2 by injectivity of h. Also H_j is holomorphic on D. Compute the expansion:

h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... .

Thus

H_j(z) = 1 / (1/z + (c_0 - z_j) + c_1 z + ... ) = z / (1 + (c_0 - z_j) z + c_1 z^2 + ... ) = z (1 - (c_0 - z_j) z + ... ) = z - (c_0 - z_j) z^2 + ... .

So H_j(z) = z + a_2^{(j)} z^2 + ... with a_2^{(j)} = -(c_0 - z_j) = z_j - c_0.

Thus H_j is a normalized univalent function (injective, H_j(0)=0, H_j'(0)=1). By part (e), |a_2^{(j)}| <= 2. Hence |z_j - c_0| <= 2 for j=1,2. By the triangle inequality,

|z_1 - z_2| <= |z_1 - c_0| + |z_2 - c_0| <= 2 + 2 = 4.

This completes part (f).

Part (g) details:

Let f be injective on D with f(0)=0, f'(0)=1. Suppose for contradiction that there exists w in C with |w| < 1/4 and w not in f(D). Consider the function

h(z) = 1/f(z), defined for z in D \ {0}. Since f is injective and f(0)=0, f(z) != 0 for z != 0, so h is holomorphic and injective on D \ {0}. Near 0, f(z) = z + O(z^2), so h(z) = 1/z + O(1). Thus h has a simple pole at 0 and can be written as h(z) = 1/z + C_0 + C_1 z + ... . Since f avoids w, h avoids 1/w. Also h avoids 0 because f(z) is finite and nonzero for z != 0. Thus h avoids 0 and 1/w.

Apply part (f) to h with z_1 = 0 and z_2 = 1/w. Then |0 - 1/w| <= 4, i.e., 1/|w| <= 4, so |w| >= 1/4. This contradicts |w| < 1/4. Therefore no such w exists, and D_{1/4}(0) subset f(D).

To see that 1/4 is best possible, consider the Koebe function

K(z) = z/(1 - z)^2 = sum_{n=1}^\infty n z^n.

It is injective on D, K(0)=0, K'(0)=1. Its image is C \ (-infty, -1/4]. In particular, it omits the value -1/4, which has modulus 1/4. Thus the radius cannot be increased.

This completes the proof of the Koebe-Bieberbach theorem.

Now we need to write this in a clear, rigorous manner. We should also ensure that we address the "compute f_n'(0), and discuss" part in (a). We have f_n'(0) = 1/n -> 0. The discussion is that without a lower bound on f'(0), the image can be shrunk arbitrarily.

Also, in part (b), we should compute f_epsilon'(0) = 1, as required.

We should also ensure that in part (c), we justify the area formula carefully. The area of the complement is nonnegative, leading to the inequality.

In part (d), we need to verify that g is indeed injective. The argument using squaring is good.

In part (e), we need to be careful about the equality case. The area theorem equality case: if sum n|c_n|^2 = 1, then the area of the complement is zero. This implies that the image of the circle |z|=rho has area zero in the limit? Actually, the area of the complement is pi(1/rho^2 - sum n|c_n|^2 rho^{2n}). If sum n|c_n|^2 = 1, then the area is pi(1/rho^2 - rho^2). As rho->1, this tends to 0. But for each rho<1, the area is positive unless the sum is exactly 1/rho^2? Wait, the inequality is sum n|c_n|^2 rho^{2n} <= 1/rho^2. If sum n|c_n|^2 = 1, then for rho<1, sum n|c_n|^2 rho^{2n} < sum n|c_n|^2 = 1 <= 1/rho^2? Actually, 1/rho^2 > 1. So the inequality is strict for rho<1. The area is pi(1/rho^2 - sum n|c_n|^2 rho^{2n}) > 0 unless the sum equals 1/rho^2. But sum n|c_n|^2 = 1 does not imply sum n|c_n|^2 rho^{2n} = 1/rho^2. So the area is positive for each rho<1. However, the equality case in the coefficient bound |c_1| <= 1 from sum n|c_n|^2 <= 1 occurs when all other c_n = 0 and |c_1| = 1. Because if any other c_n != 0, then sum n|c_n|^2 > |c_1|^2, so if |c_1|=1, the sum would exceed 1. Thus equality |c_1|=1 forces c_n = 0 for n >= 2. So h(z) = 1/z + c_1 z. This is the equality case.

Thus the argument in part (e) is valid: if |a_2| = 2, then |d_1| = 1, so sum n|c_n|^2 >= |d_1|^2 = 1, but sum <= 1, so equality holds, forcing all other coefficients zero.

We should also verify that the function h(z) = 1/z + c_1 z is indeed injective on the punctured disc. For |c_1|=1, h(z) = (1 + c_1 z^2)/z. If h(z1) = h(z2), then (1 + c_1 z1^2)/z1 = (1 + c_1 z2^2)/z2 => z2 + c_1 z1^2 z2 = z1 + c_1 z1 z2^2 => (z2 - z1) + c_1 z1 z2 (z1 - z2) = 0 => (z2 - z1)(1 - c_1 z1 z2) = 0. So either z1 = z2 or z1 z2 = 1/c_1. Since |z1|<1, |z2|<1, |z1 z2| < 1, but |1/c_1| = 1, so z1 z2 cannot equal 1/c_1. Thus z1 = z2. So it is injective. Good.

Now, for part (f), we need to ensure that H_j is indeed injective and normalized. We argued that H_j(z) = 1/(h(z) - z_j). Since h is injective, H_j is injective. H_j(0) = 0 because h has a pole at 0. H_j'(0) = 1 because near 0, h(z) ~ 1/z, so h(z) - z_j ~ 1/z, so H_j(z) ~ z. More precisely, H_j(z) = z - (c_0 - z_j) z^2 + ... , so H_j'(0) = 1. So H_j is normalized univalent. Then part (e) applies.

Alternatively, we could apply part (c) directly to h(z) - z_j? Let's see: h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . This is of the form required in (c). Then the coefficient c_1 in (c) is c_1 (the same for both j). That doesn't give a relation between z_1 and z_2. So the hint about 1/(h(z) - z_j) is indeed the right way.

Wait, the hint says "Look at the second coefficient in the power series expansion of 1/(h(z) - z_j)." That matches H_j. The second coefficient is the coefficient of z^2? Or coefficient of z^1? In the expansion H_j(z) = z + (z_j - c_0) z^2 + ... , the second coefficient (coefficient of z^2) is z_j - c_0. So the hint is exactly that.

Thus part (f) is solved.

Part (g) is straightforward using (f).

Now, we need to write the final answer. The user wants a complete solution with proofs for each part (a)-(g). We should present it clearly, with sections for each part, and include all reasoning.

We should also ensure that we use proper mathematical notation and formatting. Since the problem is from a markdown file with solution tags, we can provide a clean solution.

Let's write the solution.

We'll start with a brief introduction.

Then for each part:

(a) Provide the sequence f_n(z) = z/n. Show properties. Compute derivative. Conclude.

(b) Provide f_epsilon(z) = epsilon(e^{z/epsilon} - 1). Show properties. Conclude.

(c) Derive area formula. Show inequality.

(d) Construct psi and g. Show injectivity.

(e) Use g to bound a_2. Equality case.

(f) Define H_j. Apply (e). Triangle inequality.

(g) Contradiction using (f). Sharpness with Koebe function.

We should also mention that the Koebe function is f(z) = z/(1-z)^2.

Now, let's write the solution in detail.

Potential pitfalls:

- In part (c), we need to justify that the area of the complement is given by that formula. We can derive it as above.

- In part (d), we need to justify that psi exists. Since D is simply connected and f(z)/z is nowhere zero, a holomorphic square root exists. We can define psi(z) = exp((1/2) log(f(z)/z)) where log is a holomorphic branch of the logarithm. Since f(z)/z is nonzero and D is simply connected, such a branch exists. We choose the branch with psi(0)=1.

- In part (e), we need to be careful about the equality case. The area theorem gives sum n|c_n|^2 <= 1. If |c_1| = 1, then sum_{n=2}^\infty n|c_n|^2 = 0, so c_n = 0 for n >= 2. Thus h(z) = 1/z + c_1 z. Then we solve for g and f.

- In part (f), we need to ensure that H_j is indeed univalent (injective). Since h is injective, the map w -> 1/w is injective on the range of h - z_j (which avoids 0). So the composition is injective.

- In part (g), we need to ensure that h = 1/f is injective on D \ {0}. Since f is injective and f(z) != 0 for z != 0, the map w -> 1/w is injective on the range of f (which avoids 0). So h is injective. Also h has a simple pole at 0. So h satisfies the hypotheses of (c) and (f). Actually, for (f), we need h to be of the form 1/z + ... and injective on D \ {0}. Yes.

Thus the solution is complete.

Now, let's write the final answer.

---

## Model Solution

**Solution.**  
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\).  A holomorphic injection on \(\mathbb D\) is called *univalent*.  
The normalisation \(f(0)=0,\;f'(0)=1\) will be assumed whenever it is stated.

---------------------------------------------------------------------

### (a)  No uniform \(r\) without extra hypotheses

Take  
\[
f_n(z)=\frac{z}{n}\qquad (n=1,2,\dots ).
\]
Each \(f_n\) is holomorphic on \(\mathbb D\) and \(f_n(0)=0\).  
The image is the open disc of radius \(1/n\):
\[
f_n(\mathbb D)=\Bigl\{\frac{z}{n}:|z|<1\Bigr\}=D_{1/n}(0).
\]
Hence the point \(1/n\) (which lies in \(D_r(0)\) for every \(r>1/n\)) is **not** in \(f_n(\mathbb D)\).  
For any candidate radius \(r>0\) choose \(n>1/r\); then \(1/n\in D_r(0)\setminus f_n(\mathbb D)\), so
\(D_r(0)\not\subseteq f_n(\mathbb D)\).  Thus no single \(r\) works for all holomorphic \(f\) with \(f(0)=0\).

The derivative at the origin is \(f_n'(0)=1/n\to 0\).  This shows that the condition \(f'(0)=1\) is essential: without it the map can shrink the disc arbitrarily near the origin.

---------------------------------------------------------------------

### (b)  The condition \(f'(0)=1\) is still not enough

For \(\epsilon>0\) define  
\[
f_\epsilon(z)=\epsilon\bigl(e^{z/\epsilon}-1\bigr).
\]
Then \(f_\epsilon(0)=0\) and \(f_\epsilon'(0)=e^0=1\).  The function is entire, hence holomorphic on \(\mathbb D\).  
Since \(e^{z/\epsilon}\neq 0\) for all \(z\), we have \(f_\epsilon(z)\neq -\epsilon\); thus \(-\epsilon\notin f_\epsilon(\mathbb D)\).

Given any \(r>0\), choose \(\epsilon<r\).  Then \(-\epsilon\in D_r(0)\) but \(-\epsilon\notin f_\epsilon(\mathbb D)\).  
Hence no uniform \(r\) exists even when \(f'(0)=1\).

---------------------------------------------------------------------

### (c)  The area theorem

Let  
\[
h(z)=\frac1z+c_0+c_1z+c_2z^2+\cdots
\]
be analytic and injective for \(0<|z|<1\).  Fix \(0<\rho<1\) and consider the punctured disc
\(D_\rho^*=\{z:0<|z|<\rho\}\).  Because \(h\) is injective, the image \(h(D_\rho^*)\) is a domain.
The boundary of the complement consists of the curve \(\gamma_\rho(\theta)=h(\rho e^{i\theta})\),
traversed clockwise (since \(h(z)\sim 1/z\) near \(0\)).  The bounded component of the complement,
call it \(K_\rho\), is a compact set whose area we compute.

The signed area enclosed by a closed curve \(w(\theta)\) is \(\frac1{2i}\int_0^{2\pi}\overline{w}\,w'\,d\theta\).
For a clockwise curve this equals \(-\operatorname{Area}(K_\rho)\).  Using the series,
\[
\begin{aligned}
\gamma_\rho(\theta)&=\rho^{-1}e^{-i\theta}+\sum_{n=0}^\infty c_n\rho^n e^{in\theta},\\
\gamma_\rho'(\theta)&=-i\rho^{-1}e^{-i\theta}+\sum_{n=1}^\infty in c_n\rho^n e^{in\theta}.
\end{aligned}
\]
Multiplying and integrating, only terms with exponent \(0\) survive:
\[
\int_0^{2\pi}\overline{\gamma_\rho}\,\gamma_\rho'\,d\theta
=2\pi i\Bigl(\sum_{n=1}^\infty n|c_n|^2\rho^{2n}-\rho^{-2}\Bigr).
\]
Hence
\[
\operatorname{Area}(K_\rho)=-\frac1{2i}\int_0^{2\pi}\overline{\gamma_\rho}\,\gamma_\rho'\,d\theta
=\pi\Bigl(\rho^{-2}-\sum_{n=1}^\infty n|c_n|^2\rho^{2n}\Bigr).
\]
Since area is non‑negative,
\[
\sum_{n=1}^\infty n|c_n|^2\rho^{2n}\le \rho^{-2}\qquad(0<\rho<1).
\]
Letting \(\rho\to1^-\) (monotone convergence) yields
\[
\boxed{\sum_{n=1}^\infty n|c_n|^2\le 1}.
\]

---------------------------------------------------------------------

### (d)  Constructing an odd square root

Let \(f(z)=z+a_2z^2+\cdots\) be univalent on \(\mathbb D\).  
Because \(f\) is injective and \(f(0)=0\), we have \(f(z)\neq0\) for \(z\neq0\); thus
\(f(z)/z\neq0\) on \(\mathbb D\).  The function \(f(z)/z\) is holomorphic on the simply connected
domain \(\mathbb D\) and nowhere zero, so it possesses a holomorphic square root \(\psi\) with
\(\psi(0)=1\):
\[
\psi(z)^2=\frac{f(z)}{z}.
\]
Define
\[
g(z)=z\,\psi(z^2).
\]
Then \(g(0)=0\) and
\[
g'(0)=\psi(0)=1.
\]
Injectivity of \(g\): if \(g(z_1)=g(z_2)\), squaring gives
\(z_1^2\psi(z_1^2)^2=z_2^2\psi(z_2^2)^2\), i.e. \(f(z_1^2)=f(z_2^2)\).
By injectivity of \(f\), \(z_1^2=z_2^2\), so \(z_2=\pm z_1\).  If \(z_2=-z_1\) then
\(g(z_2)=g(-z_1)=-g(z_1)\), forcing \(g(z_1)=0\) and hence \(z_1=0\).  Thus \(z_1=z_2\).
Finally,
\[
g(z)^2=z^2\psi(z^2)^2=z^2\frac{f(z^2)}{z^2}=f(z^2).
\]
So \(g\) satisfies the same normalisation and is univalent, and \(g^2(z)=f(z^2)\).

---------------------------------------------------------------------

### (e)  The second coefficient satisfies \(|a_2|\le 2\)

From part (d), \(g\) is odd: \(g(-z)=-g(z)\).  Hence its expansion contains only odd powers:
\[
g(z)=z+b_3z^3+b_5z^5+\cdots.
\]
Comparing \(f(z^2)=g(z)^2\) gives \(a_2=2b_3\).

Now consider \(h(z)=1/g(z)\).  Since \(g\) is univalent and \(g(0)=0\), \(h\) is analytic and
injective on \(0<|z|<1\) with a simple pole at \(0\):
\[
h(z)=\frac1z+d_0+d_1z+d_2z^2+\cdots.
\]
Because \(g\) is odd, \(h\) is odd, so \(d_0=d_2=\cdots=0\):
\[
h(z)=\frac1z+d_1z+\cdots.
\]
Applying part (c) to \(h\) gives \(|d_1|\le 1\).

To relate \(d_1\) to \(a_2\), expand \(1/g\):
\[
g(z)=z\Bigl(1+\frac{a_2}{2}z^2+\cdots\Bigr)\quad\Longrightarrow\quad
\frac1{g(z)}=\frac1z\Bigl(1-\frac{a_2}{2}z^2+\cdots\Bigr)=\frac1z-\frac{a_2}{2}z+\cdots.
\]
Thus \(d_1=-a_2/2\), and \(|a_2|=2|d_1|\le 2\).

**Equality case.**  If \(|a_2|=2\) then \(|d_1|=1\).  In the inequality of part (c),
\(\sum n|c_n|^2\ge |d_1|^2=1\); together with \(\sum n|c_n|^2\le1\) this forces
\(c_n=0\) for all \(n\ge2\) and \(|c_1|=1\).  Hence \(h(z)=1/z+d_1z\) with \(|d_1|=1\).
Writing \(d_1=-e^{i\theta}\) and solving for \(g\):
\[
\frac1{g(z)}=\frac1z-e^{i\theta}z\;\Longrightarrow\;
g(z)=\frac{z}{1+e^{i\theta}z^2}.
\]
Then
\[
f(z^2)=g(z)^2=\frac{z^2}{(1+e^{i\theta}z^2)^2}
\;\Longrightarrow\;
f(z)=\frac{z}{(1+e^{i\theta}z)^2}.
\]
Replacing \(e^{i\theta}\) by \(e^{-i\theta}\) gives the stated form
\(f(z)=z/(1-e^{i\theta}z)^2\).  Conversely, for such \(f\) one computes \(a_2=2e^{i\theta}\),
so \(|a_2|=2\).

---------------------------------------------------------------------

### (f)  Two omitted values are at distance at most \(4\)

Let \(h(z)=1/z+c_0+c_1z+\cdots\) be injective on \(\mathbb D\) and suppose \(h\) avoids
\(z_1\) and \(z_2\).  For \(j=1,2\) define
\[
H_j(z)=\frac1{h(z)-z_j}.
\]
Because \(h\) avoids \(z_j\), the denominator never vanishes; because \(h\) has a simple pole
at \(0\), \(H_j\) has a simple zero at \(0\).  Injectivity of \(h\) implies injectivity of
\(H_j\).  Expanding near \(0\):
\[
h(z)-z_j=\frac1z+(c_0-z_j)+c_1z+\cdots
\;\Longrightarrow\;
H_j(z)=\frac{z}{1+(c_0-z_j)z+\cdots}=z+(z_j-c_0)z^2+\cdots.
\]
Thus \(H_j\) is normalised univalent: \(H_j(0)=0,\;H_j'(0)=1\).  By part (e), the second
coefficient satisfies \(|z_j-c_0|\le 2\) for each \(j\).  Therefore
\[
|z_1-z_2|\le|z_1-c_0|+|z_2-c_0|\le 2+2=4.
\]

---------------------------------------------------------------------

### (g)  Proof of the Koebe–Bieberbach theorem

Let \(f\) be univalent on \(\mathbb D\) with \(f(0)=0,\;f'(0)=1\).  Suppose, for a contradiction,
that some \(w\) with \(|w|<1/4\) is omitted by \(f\).  Consider
\[
h(z)=\frac1{f(z)},\qquad z\in\mathbb D\setminus\{0\}.
\]
Since \(f\) is injective and \(f(z)\neq0\) for \(z\neq0\), \(h\) is injective and holomorphic on
\(\mathbb D\setminus\{0\}\).  Near \(0\), \(f(z)=z+O(z^2)\), so \(h(z)=1/z+O(1)\); thus \(h\) has a
simple pole at \(0\) and can be written as \(h(z)=1/z+C_0+C_1z+\cdots\).
Because \(f\) avoids \(w\) and \(0\), \(h\) avoids \(1/w\) and \(0\).

Apply part (f) to \(h\) with the two omitted values \(z_1=0\) and \(z_2=1/w\):
\[
\Bigl|0-\frac1w\Bigr|\le 4\quad\Longrightarrow\quad\frac1{|w|}\le4\quad\Longrightarrow\quad|w|\ge\frac14,
\]
contradicting \(|w|<1/4\).  Hence no such \(w\) exists; i.e.
\[
D_{1/4}(0)\subseteq f(\mathbb D).
\]

**Sharpness.**  The Koebe function
\[
K(z)=\frac{z}{(1-z)^2}=z+2z^2+3z^3+\cdots
\]
is univalent on \(\mathbb D\), normalised, and its image is \(\mathbb C\setminus(-\infty,-1/4]\).
Thus the value \(-1/4\) (of modulus exactly \(1/4\)) is omitted, showing that the radius \(1/4\)
cannot be improved.

This completes the proof of the Koebe–Bieberbach radius theorem.  ∎

---

## Reasoning Details (raw)

```json
[
  {
    "type": "reasoning.text",
    "text": "We need to solve the problem completely, with full proofs for each part (a)-(g). The problem is about the Koebe-Bieberbach radius theorem for normalized univalent functions. We need to provide a rigorous solution.\n\nLet's parse the problem carefully.\n\nWe have a holomorphic map f: D -> C with f(0)=0. By open mapping theorem, image contains a small disc centered at origin. Question: does there exist r>0 such that for all f with f(0)=0, we have D_r(0) subset f(D)?\n\n(a) Show that with no further restrictions on f, no such r exists. It suffices to find a sequence of functions {f_n} holomorphic in D such that 1/n not in f_n(D). Compute f_n'(0), and discuss.\n\n(b) Assume in addition that f also satisfies f'(0)=1. Show that despite this new assumption, there exists no r>0 satisfying the desired condition. Hint: Try f_epsilon(z) = epsilon(e^{z/epsilon} - 1).\n\nThe Koebe-Bieberbach theorem states that if in addition to f(0)=0 and f'(0)=1 we also assume that f is injective, then such an r exists and the best possible value is r=1/4.\n\n(c) As a first step, show that if h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... is analytic and injective for 0<|z|<1, then sum_{n=1}^\\infty n|c_n|^2 <= 1. Hint: Calculate the area of the complement of h(D_r(0) - {0}) where 0<rho<1, and let rho->1.\n\n(d) If f(z) = z + a_2 z^2 + ... satisfies the hypotheses of the theorem, show that there exists another function g satisfying the hypotheses of the theorem such that g^2(z) = f(z^2). Hint: f(z)/z is nowhere vanishing so there exists psi such that psi^2(z) = f(z)/z and psi(0)=1. Check that g(z) = z psi(z^2) is injective.\n\n(e) With the notation of the previous part, show that |a_2| <= 2, and that equality holds iff f(z) = z/(1 - e^{i theta} z)^2 for some theta in R. Hint: What is the power series expansion of 1/g(z)? Use part (c).\n\n(f) If h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... is injective on D and avoids the values z_1 and z_2, show that |z_1 - z_2| <= 4. Hint: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).\n\n(g) Complete the proof of the theorem. Hint: If f avoids w, then 1/f avoids 0 and 1/w.\n\nWe need to provide full proofs for each part. Let's do it step by step.\n\nFirst, some background: D = unit disc {z in C: |z|<1}. Univalent means injective holomorphic.\n\nPart (a): Without further restrictions, no uniform r exists.\n\nWe need to find a sequence f_n holomorphic on D, f_n(0)=0, such that 1/n not in f_n(D). Then for any r>0, choose n large enough so that 1/n < r, then 1/n is in D_r(0) but not in f_n(D), so D_r(0) not subset of f_n(D).\n\nThe simplest: f_n(z) = z/n. Then f_n(0)=0, holomorphic. f_n(D) = {z/n: |z|<1} = D_{1/n}(0). Then 1/n is not in f_n(D) because |1/n| = 1/n, but the disc is open, so points with modulus < 1/n. Actually 1/n is on the boundary, not in the open disc. So 1/n not in f_n(D). Also f_n'(0) = 1/n -> 0. So the derivative at 0 can be arbitrarily small, which is why no uniform r exists.\n\nAlternatively, we could use f_n(z) = z/n + ... but the hint says compute f_n'(0) and discuss. So we should mention that f_n'(0) = 1/n -> 0, so the condition f'(0)=1 is necessary to prevent scaling down.\n\nPart (b): With f'(0)=1, still no uniform r.\n\nHint: f_epsilon(z) = epsilon(e^{z/epsilon} - 1). Let's check: f_epsilon(0) = epsilon(1-1)=0. f_epsilon'(z) = epsilon * (1/epsilon) e^{z/epsilon} = e^{z/epsilon}. So f_epsilon'(0) = 1. Good.\n\nNow, f_epsilon(D) = {epsilon(e^{z/epsilon} - 1): |z|<1}. Since e^{w} never equals 0, e^{z/epsilon} != 0, so f_epsilon(z) != -epsilon. Thus -epsilon is omitted. For any r>0, choose epsilon < r. Then -epsilon is in D_r(0) (since |-epsilon| = epsilon < r), but -epsilon not in f_epsilon(D). So no uniform r works.\n\nWe should also note that f_epsilon is holomorphic on D (entire). So this shows that even with f'(0)=1, the image can omit a point arbitrarily close to 0.\n\nPart (c): Area theorem.\n\nWe have h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... analytic and injective for 0<|z|<1. We need to show sum_{n=1}^\\infty n|c_n|^2 <= 1.\n\nThe hint: Calculate the area of the complement of h(D_r(0) \\ {0}) where 0<rho<1, and let rho->1.\n\nLet's denote D_r = {z: |z|<r}. Then h is injective on the punctured disc D_r \\ {0}. The image is h(D_r \\ {0}). Since h has a simple pole at 0, the image covers the exterior of some region. The complement of h(D_r \\ {0}) in C is a compact set (since h maps the boundary |z|=r to a closed curve, and by injectivity, the image of the punctured disc is the exterior of the image of the circle, maybe with some orientation). Actually, for univalent functions on an annulus or punctured disc, the area of the complement can be computed via the area theorem.\n\nLet's compute the area of the complement of h(D_r \\ {0}). Since h is injective on 0<|z|<r, the image of the punctured disc is a domain. The complement is the set of points not hit. Because h has a simple pole at 0, near 0, h(z) ~ 1/z, so the image of a small circle |z|=epsilon is a large circle of radius ~1/epsilon. As epsilon->0, the image covers the exterior of a large disc. The complement of h(D_r \\ {0}) is contained in the image of the annulus r<|z|<1? Wait, h is defined on 0<|z|<1. So for a fixed r<1, h is defined on D_r \\ {0}. The complement of h(D_r \\ {0}) is a compact set (since h maps the boundary |z|=r to a closed curve, and the point at infinity is in the image because of the pole). Actually, the image of D_r \\ {0} is the exterior of some compact set K_r (the image of the annulus r<|z|<1? No, h is not defined outside D_r). Let's think carefully.\n\nh is defined on the punctured unit disc. For 0<rho<1, consider the image of the punctured disc D_rho \\ {0}. Since h is injective, the image is a domain. The boundary consists of the image of the circle |z|=rho and possibly the image of the puncture (which goes to infinity). Because h has a simple pole at 0, the image of a small circle around 0 is a large curve that winds around infinity. The complement of h(D_rho \\ {0}) is a compact set contained in the image of the annulus rho<|z|<1? Actually, h is defined on the whole punctured unit disc, but we are only looking at the image of D_rho \\ {0}. The complement of this image is the set of points w such that h(z) != w for all 0<|z|<rho. Since h is injective, the equation h(z)=w has at most one solution. For |w| large, there is a solution near 0 (because of the pole). So the complement is bounded. In fact, the complement is contained in h({rho<|z|<1})? No, h({rho<|z|<1}) is the image of the annulus, which is disjoint from h(D_rho \\ {0}) by injectivity. So the complement of h(D_rho \\ {0}) contains h({rho<|z|<1}) and possibly some other points? Actually, since h is injective on the whole punctured disc, the images of D_rho \\ {0} and the annulus rho<|z|<1 are disjoint. The union of these two images is h(D_1 \\ {0}). The complement of h(D_rho \\ {0}) in C is the union of the complement of h(D_1 \\ {0}) and the image of the annulus? Wait, h(D_1 \\ {0}) is the image of the whole punctured disc. The complement of h(D_rho \\ {0}) includes all points not hit by h on D_rho \\ {0}. This includes the image of the annulus (since those points are hit only there), and also points not hit anywhere (the omitted set of h on the whole punctured disc). But h is injective, so it could omit some values. The complement of h(D_1 \\ {0}) is the omitted set. So the complement of h(D_rho \\ {0}) is the union of the omitted set and the image of the annulus rho<|z|<1.\n\nBut the area theorem is usually proved by computing the area of the complement of h(D_rho \\ {0}) in two ways: one using the parametrization of the boundary, and one using the series expansion.\n\nStandard proof of area theorem: For h(z) = 1/z + sum_{n=0}^\\infty c_n z^n, injective on 0<|z|<1. For 0<rho<1, consider the image of the circle |z|=rho. The area of the complement of h(D_rho \\ {0}) is given by pi(1/rho^2 - sum_{n=1}^\\infty n|c_n|^2 rho^{2n}). Then let rho->1 to get the inequality.\n\nLet's derive this carefully.\n\nLet w = h(z). For z on the circle |z|=rho, we have z = rho e^{i theta}. Then h(z) = 1/(rho e^{i theta}) + sum_{n=0}^\\infty c_n rho^n e^{i n theta}. The image of the circle is a closed curve (maybe self-intersecting? But since h is injective on the punctured disc, the image of the circle is a simple closed curve? Actually, h is injective on the punctured disc, so the image of the circle |z|=rho is a simple closed curve (Jordan curve) because if h(z1)=h(z2) for |z1|=|z2|=rho, then z1=z2 by injectivity. So it's a simple closed curve. The image of the punctured disc D_rho \\ {0} is the exterior of this curve (since near 0, h(z) is large). So the complement of h(D_rho \\ {0}) is the bounded region enclosed by this curve (including the curve itself). The area of this region can be computed using Green's theorem or the formula for area enclosed by a parametric curve.\n\nThe area enclosed by a parametric curve w(theta) = h(rho e^{i theta}) for theta from 0 to 2pi is given by (1/2) Im integral_{0}^{2pi} overline{w} w'(theta) d theta? Actually, the area of the region enclosed by a simple closed curve parameterized by w(theta) is (1/2) Im integral_0^{2pi} overline{w} dw/d theta d theta. Or equivalently, (1/2) integral_0^{2pi} (x dy - y dx). In complex notation, area = (1/2i) integral overline{w} w' d theta.\n\nBut we need the area of the complement, which is the interior of the curve. Since h is injective, the image of the punctured disc is the exterior, so the complement is the interior. The area of the interior is given by the same formula but with opposite sign? Let's check orientation. As theta increases, z = rho e^{i theta} goes counterclockwise. Near 0, h(z) ~ 1/z, so w ~ (1/rho) e^{-i theta}. As theta increases, the argument of w decreases, so the image of the circle is traversed clockwise. Thus the interior is on the right side? Let's compute carefully.\n\nStandard area theorem: For h(z) = 1/z + sum_{n=0}^\\infty c_n z^n, univalent in 0<|z|<1, the area of the complement of h(D_rho \\ {0}) is pi(1/rho^2 - sum_{n=1}^\\infty n|c_n|^2 rho^{2n}). Since area is nonnegative, we get the inequality.\n\nLet's derive it.\n\nLet w = h(z). The boundary of the complement is the image of |z|=rho. The area of the complement (the interior) is given by:\n\nA = (1/2i) integral_{|z|=rho} overline{w} dw.\n\nBut dw = h'(z) dz. So A = (1/2i) integral_{|z|=rho} overline{h(z)} h'(z) dz.\n\nParameterize z = rho e^{i theta}, dz = i rho e^{i theta} d theta.\n\nThen h(z) = 1/(rho e^{i theta}) + sum_{n=0}^\\infty c_n rho^n e^{i n theta}.\n\noverline{h(z)} = 1/(rho e^{-i theta}) + sum_{n=0}^\\infty overline{c_n} rho^n e^{-i n theta}.\n\nh'(z) = -1/z^2 + sum_{n=1}^\\infty n c_n z^{n-1} = -1/(rho^2 e^{2i theta}) + sum_{n=1}^\\infty n c_n rho^{n-1} e^{i (n-1) theta}.\n\nThen overline{h(z)} h'(z) dz = [overline{h(z)} h'(z)] i rho e^{i theta} d theta.\n\nSo A = (1/2i) integral_0^{2pi} overline{h(rho e^{i theta})} h'(rho e^{i theta}) i rho e^{i theta} d theta = (rho/2) integral_0^{2pi} overline{h} h' e^{i theta} d theta.\n\nAlternatively, use the formula A = (1/2) Im integral overline{w} dw. But let's compute directly.\n\nCompute overline{h(z)} h'(z) dz. Since dz = i z d theta / rho? Actually z = rho e^{i theta}, so dz = i z d theta. So overline{h} h' dz = overline{h} h' i z d theta.\n\nThus A = (1/2i) integral_0^{2pi} overline{h} h' i z d theta = (1/2) integral_0^{2pi} overline{h} h' z d theta.\n\nNow substitute series.\n\nh(z) = z^{-1} + sum_{n=0}^\\infty c_n z^n.\noverline{h(z)} = z^{-1} (since |z|=rho, overline{z^{-1}} = overline{z}^{-1} = (rho e^{-i theta})^{-1} = rho^{-1} e^{i theta} = z/rho^2? Wait, careful: overline{z} = rho e^{-i theta} = rho^2 / z? Actually z = rho e^{i theta}, so overline{z} = rho e^{-i theta} = rho^2 / (rho e^{i theta}) = rho^2 / z. So overline{z^{-1}} = overline{z}^{-1} = (rho^2 / z)^{-1} = z / rho^2. But also z^{-1} = e^{-i theta}/rho. Its conjugate is e^{i theta}/rho = z/rho^2. Yes.\n\nSo overline{h(z)} = overline{z^{-1}} + sum_{n=0}^\\infty overline{c_n} overline{z}^n = z/rho^2 + sum_{n=0}^\\infty overline{c_n} (rho^2 / z)^n? Wait, overline{z}^n = (rho^2 / z)^n = rho^{2n} z^{-n}. That seems messy. Better to use the parameterization directly.\n\nLet's use the parameterization w(theta) = h(rho e^{i theta}). Then the area enclosed by the curve w(theta) (traversed clockwise) is given by A = (1/2) integral_0^{2pi} Im( overline{w} w' ) d theta? Actually, the area of a region bounded by a simple closed curve parameterized by w(theta) is (1/2) integral_0^{2pi} (x dy - y dx) = (1/2i) integral_0^{2pi} overline{w} w' d theta. This formula gives the signed area, positive if the curve is traversed counterclockwise. Since our curve is traversed clockwise (because of the 1/z term), the signed area will be negative of the interior area. But the complement is the interior, so we take absolute value or adjust sign.\n\nLet's compute I = integral_0^{2pi} overline{w} w' d theta.\n\nw(theta) = rho^{-1} e^{-i theta} + sum_{n=0}^\\infty c_n rho^n e^{i n theta}.\noverline{w(theta)} = rho^{-1} e^{i theta} + sum_{n=0}^\\infty overline{c_n} rho^n e^{-i n theta}.\nw'(theta) = derivative w.r.t theta: -i rho^{-1} e^{-i theta} + sum_{n=1}^\\infty i n c_n rho^n e^{i n theta}.\n\nNow multiply overline{w} and w':\n\noverline{w} w' = [rho^{-1} e^{i theta} + sum_{m=0}^\\infty overline{c_m} rho^m e^{-i m theta}] * [-i rho^{-1} e^{-i theta} + sum_{n=1}^\\infty i n c_n rho^n e^{i n theta}].\n\nExpand:\n\nTerm 1: (rho^{-1} e^{i theta}) * (-i rho^{-1} e^{-i theta}) = -i rho^{-2}.\n\nTerm 2: (rho^{-1} e^{i theta}) * (sum_{n=1}^\\infty i n c_n rho^n e^{i n theta}) = i rho^{-1} sum_{n=1}^\\infty n c_n rho^n e^{i (n+1) theta}.\n\nTerm 3: (sum_{m=0}^\\infty overline{c_m} rho^m e^{-i m theta}) * (-i rho^{-1} e^{-i theta}) = -i rho^{-1} sum_{m=0}^\\infty overline{c_m} rho^m e^{-i (m+1) theta}.\n\nTerm 4: (sum_{m=0}^\\infty overline{c_m} rho^m e^{-i m theta}) * (sum_{n=1}^\\infty i n c_n rho^n e^{i n theta}) = i sum_{m=0}^\\infty sum_{n=1}^\\infty n overline{c_m} c_n rho^{m+n} e^{i (n-m) theta}.\n\nNow integrate over theta from 0 to 2pi. The integral of e^{i k theta} over 0 to 2pi is 0 unless k=0, in which case it's 2pi.\n\nTerm 1: constant -i rho^{-2}. Integral = -i rho^{-2} * 2pi.\n\nTerm 2: exponent i (n+1) theta. Since n>=1, n+1 >=2, never zero. So integral = 0.\n\nTerm 3: exponent -i (m+1) theta. Since m>=0, m+1 >=1, never zero. So integral = 0.\n\nTerm 4: exponent i (n-m) theta. This is zero unless n=m. So we need n=m. But n>=1, m>=0. So m can be 0,1,2,... and n=m. So for each n>=1, m=n. Then term is i * n overline{c_n} c_n rho^{2n} e^{i 0} = i n |c_n|^2 rho^{2n}. Also m=0, n=0? But n starts at 1, so m=0 gives n=0 not allowed. So only n=m>=1.\n\nThus integral of term 4 = i * 2pi * sum_{n=1}^\\infty n |c_n|^2 rho^{2n}.\n\nWait, check: term 4 is i sum_{m,n} ... e^{i(n-m)theta}. When n=m, the sum over m from 0 to infinity, n=m, but n>=1, so m>=1. So sum_{n=1}^\\infty i n |c_n|^2 rho^{2n}. Then integral over theta gives 2pi times that.\n\nSo total integral I = integral_0^{2pi} overline{w} w' d theta = -i 2pi rho^{-2} + i 2pi sum_{n=1}^\\infty n |c_n|^2 rho^{2n}.\n\nThus I = 2pi i (sum_{n=1}^\\infty n |c_n|^2 rho^{2n} - rho^{-2}).\n\nNow the area A of the complement (interior) is given by A = (1/2) |Im(I)|? Actually, the formula A = (1/2i) integral overline{w} w' d theta gives the signed area. For a clockwise curve, the signed area is negative of the geometric area. Let's compute (1/2i) I.\n\n(1/2i) I = (1/2i) * 2pi i (sum n|c_n|^2 rho^{2n} - rho^{-2}) = pi (sum n|c_n|^2 rho^{2n} - rho^{-2}).\n\nSince the curve is traversed clockwise, the signed area is negative of the interior area. The interior area is positive. So interior area = - (1/2i) I = pi (rho^{-2} - sum n|c_n|^2 rho^{2n}).\n\nThus the area of the complement of h(D_rho \\ {0}) is pi (1/rho^2 - sum_{n=1}^\\infty n|c_n|^2 rho^{2n}).\n\nSince area is nonnegative, we have 1/rho^2 - sum_{n=1}^\\infty n|c_n|^2 rho^{2n} >= 0, i.e., sum_{n=1}^\\infty n|c_n|^2 rho^{2n} <= 1/rho^2.\n\nNow let rho -> 1^-. By monotone convergence (or just continuity), sum_{n=1}^\\infty n|c_n|^2 <= 1.\n\nThis proves part (c).\n\nWe should also note that h is injective on the punctured disc, so the image of the circle is a simple closed curve, and the area formula holds.\n\nPart (d): Given f(z) = z + a_2 z^2 + ... injective on D, f(0)=0, f'(0)=1. Show there exists g satisfying the same hypotheses such that g^2(z) = f(z^2).\n\nHint: f(z)/z is nowhere vanishing. Since f is injective and f(0)=0, f(z) != 0 for z != 0. So f(z)/z != 0 for all z in D. Also f(z)/z is holomorphic on D (removable singularity at 0, with value f'(0)=1). Since D is simply connected and f(z)/z is nowhere zero, there exists a holomorphic square root psi(z) such that psi(z)^2 = f(z)/z and psi(0)=1 (choose the branch with positive value at 0). Then define g(z) = z psi(z^2). Then g(0)=0. Compute g'(0): g(z) = z (1 + (a_2/2) z^2 + ...)? Let's compute: f(z)/z = 1 + a_2 z + a_3 z^2 + ... . The square root psi(z) = 1 + (a_2/2) z + ... . Then psi(z^2) = 1 + (a_2/2) z^2 + ... . So g(z) = z + (a_2/2) z^3 + ... . So g'(0)=1. Also g is injective? Need to check.\n\nHint says check that g is injective. Let's verify: Suppose g(z1) = g(z2). Then z1 psi(z1^2) = z2 psi(z2^2). Square both sides: z1^2 psi(z1^2)^2 = z2^2 psi(z2^2)^2. But psi(z^2)^2 = f(z^2)/z^2. So z1^2 * f(z1^2)/z1^2 = z2^2 * f(z2^2)/z2^2, so f(z1^2) = f(z2^2). Since f is injective, z1^2 = z2^2. So z2 = +/- z1. If z2 = z1, done. If z2 = -z1, then g(z2) = g(-z1) = -z1 psi((-z1)^2) = -z1 psi(z1^2) = -g(z1). So g(z1) = g(-z1) implies g(z1) = -g(z1), so 2g(z1)=0, so g(z1)=0. But g(z)=0 only at z=0 (since g(z)/z = psi(z^2) != 0). So z1=0, thus z2=0. So g is injective.\n\nThus g satisfies the hypotheses: g(0)=0, g'(0)=1, g injective holomorphic on D. And g^2(z) = z^2 psi(z^2)^2 = z^2 * f(z^2)/z^2 = f(z^2). Good.\n\nPart (e): Show |a_2| <= 2, equality iff f(z) = z/(1 - e^{i theta} z)^2.\n\nFrom part (d), we have g with g^2(z) = f(z^2). Also g(z) = z + b_2 z^3 + ... (odd function). Actually, g is odd? Let's check: g(-z) = -z psi((-z)^2) = -z psi(z^2) = -g(z). So g is odd. So its power series has only odd powers: g(z) = z + b_3 z^3 + b_5 z^5 + ... . But the hint says g(z) = z psi(z^2) and psi(z) = 1 + (a_2/2) z + ... . So psi(z^2) = 1 + (a_2/2) z^2 + ... . Thus g(z) = z + (a_2/2) z^3 + ... . So the coefficient of z^3 is a_2/2.\n\nNow consider 1/g(z). Since g has a simple zero at 0, 1/g has a simple pole at 0. Write 1/g(z) = 1/z + d_0 + d_1 z + d_2 z^2 + ... . Since g is odd, 1/g is odd? Let's check: g(-z) = -g(z), so 1/g(-z) = -1/g(z). So 1/g is odd. Thus its Laurent expansion has only odd powers: 1/g(z) = 1/z + d_1 z + d_3 z^3 + ... . So d_0 = 0, d_2 = 0, etc. In particular, the coefficient of z^1 is d_1.\n\nNow apply part (c) to h(z) = 1/g(z). Is h injective on 0<|z|<1? Since g is injective on D and g(0)=0, g maps D onto some domain. The function 1/g is defined on D \\ {0}. Is it injective? If 1/g(z1) = 1/g(z2), then g(z1) = g(z2), so z1 = z2 by injectivity of g. So yes, 1/g is injective on D \\ {0}. It has a simple pole at 0. So we can apply part (c) to h = 1/g.\n\nPart (c) says sum_{n=1}^\\infty n |c_n|^2 <= 1, where c_n are the coefficients of h(z) = 1/z + c_0 + c_1 z + ... . For h = 1/g, we have c_0 = 0, c_1 = d_1, c_2 = 0, etc. So the sum is 1*|c_1|^2 + 2*|c_2|^2 + ... = |c_1|^2 + ... <= 1. Thus |c_1| <= 1.\n\nNow we need to relate c_1 to a_2. We have g(z) = z + (a_2/2) z^3 + ... . Compute 1/g(z). Write g(z) = z (1 + (a_2/2) z^2 + ...). Then 1/g(z) = (1/z) * 1/(1 + (a_2/2) z^2 + ...) = (1/z) * (1 - (a_2/2) z^2 + ...) = 1/z - (a_2/2) z + ... . So c_1 = -a_2/2. Thus |a_2/2| <= 1, so |a_2| <= 2.\n\nEquality |a_2| = 2 means |c_1| = 1. In part (c), equality in the area theorem sum n|c_n|^2 <= 1 occurs only when h(z) = 1/z + c_1 z (i.e., all other c_n = 0). Actually, the area theorem says the area of the complement is pi(1/rho^2 - sum n|c_n|^2 rho^{2n}). If sum n|c_n|^2 = 1, then the area of the complement is pi(1/rho^2 - rho^2) (since only n=1 term). As rho->1, the area tends to 0. This means the complement has area 0, so the image of the punctured disc is dense in C? Actually, the complement is the interior of the image of the circle. If the area is zero, the image of the circle must be a curve that encloses zero area? Wait, the area of the complement is the area of the bounded component of the complement of the image of the circle. If that area is zero, the curve must be degenerate? Actually, the equality case in the area theorem corresponds to the Koebe function or rotations. For h(z) = 1/z + c_1 z, the image of the punctured disc is the complement of a line segment? Let's recall: The Koebe function is k(z) = z/(1-z)^2 = 1/z + 2z + ...? Actually, the standard Koebe function is f(z) = z/(1-z)^2 = sum_{n=1}^\\infty n z^n. Its inverse is h(w) = ...? Wait, the Koebe function maps D onto C minus a ray (-infty, -1/4]. The inverse function has a simple pole at infinity? Let's recall: The Koebe function is f(z) = z/(1-z)^2. Then f'(0)=1. It omits the value -1/4. The inverse function h(w) = ...? Actually, the inverse of the Koebe function is h(w) = (sqrt(1+w} - 1)/w? Something like that. But the standard form for the inverse of a univalent function with simple pole at infinity is h(w) = 1/w + c_1 w + ...? Wait, the Koebe function maps D onto the complement of a ray. The inverse function is defined on C \\ (-infty, -1/4] and has a simple pole at infinity? Actually, the Koebe function is univalent on D, but its inverse is defined on the complement of the omitted ray. The omitted ray is (-infty, -1/4]. The inverse function h(w) maps C \\ (-infty, -1/4] back to D. But h(w) has a simple pole at w=0? No, f(0)=0, so h(0)=0. The inverse function is holomorphic near 0. But the function h(z) = 1/f(1/z) maybe? Let's recall the standard area theorem: For a univalent function f(z) = z + a_2 z^2 + ... on D, the inverse function near infinity is h(w) = 1/w + a_2 + a_3/w + ...? Actually, if f is univalent on D, then f(1/z) is univalent near infinity. Define g(w) = 1/f(1/w). Then g(w) = 1/( (1/w) + a_2 (1/w)^2 + ... ) = w / (1 + a_2/w + ...) = w (1 - a_2/w + ...) = w - a_2 + ... . That's not a simple pole. Hmm.\n\nWait, the standard area theorem is for functions h(z) = z + b_0 + b_1/z + ... that are univalent on |z|>1. But here we have h(z) = 1/z + c_0 + c_1 z + ... univalent on 0<|z|<1. This is the same as a function univalent near infinity after inversion? Let's map: Let w = 1/z. Then h(z) = w + c_0 + c_1/w + c_2/w^2 + ... . So H(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + ... . This is univalent for |w|>1. The area theorem for such functions says sum n |c_n|^2 <= 1? Actually, the standard area theorem for H(w) = w + b_0 + sum_{n=1}^\\infty b_n / w^n univalent on |w|>1 says sum n |b_n|^2 <= 1. Here b_n = c_n. So indeed sum n|c_n|^2 <= 1. The equality case is H(w) = w + c_1 / w (i.e., c_n=0 for n!=1). This corresponds to h(z) = 1/z + c_1 z. This maps the punctured disc onto the complement of a line segment (or a ray?). Actually, h(z) = 1/z + c_1 z. If |c_1|=1, this is a rotation of the Koebe function's inverse? Let's check: The Koebe function f(z) = z/(1-z)^2 maps D onto C \\ (-infty, -1/4]. Its inverse function is h(w) = (sqrt{1+w}-1)/w? Let's compute: w = z/(1-z)^2. Solve for z: w(1 - 2z + z^2) = z => w - 2wz + w z^2 - z = 0 => w z^2 - (2w+1)z + w = 0. Using quadratic formula: z = [(2w+1) +/- sqrt((2w+1)^2 - 4w^2)]/(2w) = [(2w+1) +/- sqrt(4w+1)]/(2w). The branch that gives z=0 at w=0 is z = [(2w+1) - sqrt(1+4w)]/(2w). Expand sqrt(1+4w) = 1 + 2w - 2w^2 + ... . Then numerator = 2w+1 - (1+2w - 2w^2 + ...) = 2w^2 - ... . Divide by 2w gives w - ... . So near 0, h(w) = w + ... . That's not of the form 1/z + ... . So maybe the equality case corresponds to a different function.\n\nWait, the function h(z) = 1/z + c_1 z with |c_1|=1 maps the punctured disc onto the complement of a line segment. Let's compute: h(z) = 1/z + c_1 z. Let c_1 = e^{i alpha}. Then h(z) = (1 + c_1 z^2)/z. The image of the unit circle |z|=1 is w = e^{-i theta} + c_1 e^{i theta} = e^{-i theta} + e^{i(alpha+theta)}. This is an ellipse? Actually, as theta varies, w traces a curve. The complement of the image of the punctured disc is the image of the annulus 1<|z|<infty? No, h is defined on |z|<1. The image of |z|=r is a curve. As r->1, the curve approaches the boundary of the image of the punctured disc. The complement of the image of the punctured disc is the union of the image of the annulus 1<|z|<infty? No, h is only defined for |z|<1. The complement of h(D \\ {0}) is a compact set. For h(z) = 1/z + c_1 z, the complement is a line segment. Indeed, the Koebe function's inverse has a simple pole at infinity? Let's check the standard Koebe function: f(z) = z/(1-z)^2. Its inverse g(w) satisfies g(w) = ...? Actually, the Koebe function maps D onto C \\ (-infty, -1/4]. The inverse function is defined on C \\ (-infty, -1/4] and maps to D. Near infinity, g(w) ~ 1/w? Let's see: f(z) ~ z for small z. For large w, f(z) = w implies z ~ w? No, f(z) = z/(1-z)^2. For large w, z is near 1? Actually, f(z) has a pole at z=1. The image of D is C \\ (-infty, -1/4]. So the complement is a ray. The inverse function g(w) maps C \\ (-infty, -1/4] to D. Near w=infty, g(w) ~ 1/w? Let's compute: w = z/(1-z)^2. For large w, z is near 1? Let's solve for z near 1: let z = 1 - u, small u. Then w = (1-u)/u^2 ~ 1/u^2. So u ~ 1/sqrt{w}. Then z = 1 - 1/sqrt{w} + ... . So g(w) = 1 - 1/sqrt{w} + ... . That's not a simple pole.\n\nWait, the area theorem is usually stated for functions of the form f(z) = z + b_0 + sum_{n=1}^\\infty b_n / z^n univalent on |z|>1. The complement of the image of |z|>1 is a compact set containing infinity? Actually, the image of |z|>1 is the exterior of some compact set. The area of the complement (the bounded component) is pi(sum n|b_n|^2). Wait, the standard area theorem says: If f(z) = z + b_0 + sum_{n=1}^\\infty b_n / z^n is univalent for |z|>1, then sum_{n=1}^\\infty n |b_n|^2 <= 1. The complement of f({|z|>1}) has area pi(1 - sum n|b_n|^2). So equality holds when the complement has area zero, i.e., f maps onto the complement of a line segment (or a point?). Actually, the complement is a set of area zero, which must be a line segment (or a point). The extremal functions are rotations of the Koebe function: f(z) = z/(1 - e^{i theta}/z)^2? Let's check: The Koebe function is k(z) = z/(1-z)^2. Its inverse is h(w) = ...? Actually, the Koebe function maps D onto C \\ (-infty, -1/4]. The function that maps the exterior of the unit disc onto the complement of a line segment is something like z + 1/z? No, Joukowsky map maps exterior of unit disc to complement of [-2,2]. But the Koebe function is different.\n\nLet's recall: The Koebe function is f(z) = z/(1-z)^2 = sum_{n=1}^\\infty n z^n. It maps D onto C \\ (-infty, -1/4]. The inverse function g(w) is defined on C \\ (-infty, -1/4] and satisfies g(w) = w - 2 + 3/w - ...? Let's compute: w = z/(1-z)^2. Solve for z: z = w/(1+w)^2? No, that's the inverse of something else. Actually, the inverse of the Koebe function is g(w) = (sqrt{1+w} - 1)/w? Let's check: If z = (sqrt{1+w} - 1)/w, then compute z/(1-z)^2. Let's do it: Let s = sqrt{1+w}. Then z = (s-1)/w = (s-1)/(s^2-1) = 1/(s+1). Then 1-z = 1 - 1/(s+1) = s/(s+1). So (1-z)^2 = s^2/(s+1)^2 = (1+w)/(s+1)^2. Then z/(1-z)^2 = [1/(s+1)] / [(1+w)/(s+1)^2] = (s+1)/(1+w) = (s+1)/s^2 = 1/s^2 + 1/s = 1/(1+w) + 1/sqrt{1+w}. That's not w. So that's not the inverse.\n\nActually, the inverse of the Koebe function is g(w) = w/(1+sqrt{1-w})^2? Something like that. Let's not get bogged down. The equality case in the area theorem for h(z) = 1/z + c_1 z corresponds to the complement being a line segment. The function h(z) = 1/z + c_1 z maps the punctured disc onto the complement of a line segment. The corresponding f is the Koebe function.\n\nSpecifically, if 1/g(z) = 1/z + c_1 z, then g(z) = z/(1 + c_1 z^2). Then f(z^2) = g(z)^2 = z^2/(1 + c_1 z^2)^2. So f(w) = w/(1 + c_1 w)^2. Let e^{i theta} = -c_1? Actually, we want f(z) = z/(1 - e^{i theta} z)^2. Let's check: If f(z) = z/(1 - a z)^2 with |a|=1, then f(z^2) = z^2/(1 - a z^2)^2. Then g(z)^2 = z^2/(1 - a z^2)^2, so g(z) = +/- z/(1 - a z^2). But g must satisfy g(0)=0, g'(0)=1. Let's compute g(z) = z/(1 - a z^2). Then g'(0)=1. And g is odd? g(-z) = -z/(1 - a z^2) = -g(z). Yes. Then 1/g(z) = (1 - a z^2)/z = 1/z - a z. So c_1 = -a. Since |a|=1, |c_1|=1. So equality holds. Conversely, if |c_1|=1, then 1/g(z) = 1/z + c_1 z, so g(z) = z/(1 + c_1 z^2). Then f(z) = g(sqrt{z})^2? Actually, f(z^2) = g(z)^2 = z^2/(1 + c_1 z^2)^2. So f(w) = w/(1 + c_1 w)^2. Let e^{i theta} = -c_1. Then f(w) = w/(1 - e^{i theta} w)^2. So equality holds iff f is a rotation of the Koebe function.\n\nThus part (e) is proved.\n\nPart (f): If h(z) = 1/z + c_0 + c_1 z + ... is injective on D and avoids values z_1 and z_2, show |z_1 - z_2| <= 4.\n\nHint: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).\n\nLet's define h_j(z) = 1/(h(z) - z_j). Since h avoids z_j, h(z) - z_j != 0. Also h has a simple pole at 0, so h(z) - z_j has a simple pole at 0. Thus h_j has a simple zero at 0? Wait, h(z) ~ 1/z near 0, so h(z) - z_j ~ 1/z. Then 1/(h(z) - z_j) ~ z. So h_j has a simple zero at 0, not a pole. But the hint says 1/(h(z) - z_j) is injective and has expansion 1/z + c_0 + ...? That seems contradictory. Let's check.\n\nIf h(z) = 1/z + c_0 + c_1 z + ... , then h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . Then 1/(h(z) - z_j) = 1 / (1/z + ... ) = z / (1 + (c_0 - z_j) z + ... ) = z (1 - (c_0 - z_j) z + ... ) = z - (c_0 - z_j) z^2 + ... . So it has a simple zero at 0, not a simple pole. So the hint \"1/(h(z) - z_j) is injective and has expansion 1/z + c_0 + ...\" seems wrong? Wait, maybe the hint means something else. Let's read the hint: \"Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).\" But if h avoids z_j, then h(z) - z_j is never zero. However, h has a pole at 0, so h(z) - z_j has a pole at 0. Then 1/(h(z) - z_j) has a zero at 0. So its expansion starts with z, not 1/z. So the hint might be miswritten? Or perhaps they consider h(z) - z_j and then take reciprocal? Let's think.\n\nAlternatively, maybe they define a new function H(z) = 1/(h(z) - z_j). Since h is injective, H is also injective? If h(z1) != h(z2), then h(z1) - z_j != h(z2) - z_j, so 1/(h(z1)-z_j) != 1/(h(z2)-z_j). So yes, H is injective. H has a zero at 0. But we can consider the function k(z) = 1/H(z) = h(z) - z_j. That has a simple pole at 0. But the hint says \"1/(h(z) - z_j) is injective and has expansion 1/z + c_0 + ...\". That would be true if h(z) - z_j had a zero at 0, but it has a pole. So maybe the hint is for a different function? Let's re-read the problem statement for (f):\n\n\"(f) If h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... is injective on D and avoids the values z_1 and z_2, show that |z_1 - z_2| <= 4. [Hint: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).]\"\n\nWait, maybe they mean the function h(z) - z_j avoids 0, so we can consider its reciprocal? But the reciprocal has a zero at 0. However, we can apply a transformation to get a function with a simple pole. For example, consider the function p(z) = 1/(h(z) - z_j) - z_j? No.\n\nAlternatively, maybe the hint is to consider the function H(z) = 1/(h(z) - z_j). Since h avoids z_j, H is holomorphic and injective on D. H(0) = 0 (since h has a pole). So H(z) = z + d_2 z^2 + ... (after scaling? Actually H'(0) = ? Let's compute: h(z) = 1/z + c_0 + c_1 z + ... . Then h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . Then 1/(h(z) - z_j) = z / (1 + (c_0 - z_j) z + c_1 z^2 + ... ) = z (1 - (c_0 - z_j) z + ... ) = z - (c_0 - z_j) z^2 + ... . So H(z) = z + d_2 z^2 + ... with d_2 = -(c_0 - z_j). But H is injective and H(0)=0, H'(0)=1. So H is normalized univalent. Then we can apply the result of part (e) to H? But H is not of the form 1/z + ... . However, we can consider the inverse function? Or we can apply the area theorem to H? No, H is holomorphic on D, not on a punctured disc.\n\nWait, maybe the hint is to consider the function 1/(h(z) - z_j) and then apply part (c) to it after a change of variable? But part (c) requires a simple pole at 0. H has a simple zero at 0. So we can consider the function 1/H(z) = h(z) - z_j, which has a simple pole at 0. But 1/H is not injective? Actually, if H is injective, then 1/H is also injective (since w -> 1/w is injective on C\\{0}). But 1/H = h - z_j has a simple pole at 0. So we can apply part (c) to 1/H? Let's check: 1/H(z) = h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . This is of the form 1/z + C_0 + C_1 z + ... . And it's injective on 0<|z|<1 (since h is injective and subtracting z_j doesn't change injectivity). So we can apply part (c) to this function. Then the coefficient c_1 in part (c) for this function is c_1 (the same as in h). But we need to relate z_1 and z_2.\n\nAlternatively, consider the function H_j(z) = 1/(h(z) - z_j). This is injective and holomorphic on D, with H_j(0)=0, H_j'(0)=1. So H_j is normalized univalent. Then by part (e), the coefficient of z^2 in H_j is bounded by 2 in absolute value. The coefficient of z^2 in H_j is -(c_0 - z_j) = z_j - c_0. So |z_j - c_0| <= 2? Wait, H_j(z) = z + d_2 z^2 + ... . Then by part (e), |d_2| <= 2. But d_2 = -(c_0 - z_j) = z_j - c_0. So |z_j - c_0| <= 2 for each j=1,2. Then by triangle inequality, |z_1 - z_2| <= |z_1 - c_0| + |z_2 - c_0| <= 2 + 2 = 4. That gives the result! And the hint says \"Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).\" Indeed, the second coefficient (coefficient of z^2? Or coefficient of z^1? Wait, H_j(z) = 1/(h(z) - z_j) = z + (z_j - c_0) z^2 + ... . The second coefficient is the coefficient of z^2, which is z_j - c_0. So the hint is exactly that.\n\nBut wait, part (e) applies to functions f(z) = z + a_2 z^2 + ... injective. Here H_j(z) = 1/(h(z) - z_j) is injective? Let's verify: h is injective, so h(z1) != h(z2) for z1 != z2. Then h(z1) - z_j != h(z2) - z_j. Since the map w -> 1/w is injective on C \\ {0}, we have 1/(h(z1) - z_j) != 1/(h(z2) - z_j). So H_j is injective. Also H_j is holomorphic on D because h(z) - z_j != 0 for all z in D (since h avoids z_j). And H_j(0) = 0 because h has a pole at 0, so h(z) - z_j ~ 1/z, so 1/(h(z)-z_j) ~ z. More precisely, H_j(z) = z - (c_0 - z_j) z^2 + ... . So H_j'(0) = 1. Thus H_j satisfies the hypotheses of the theorem (normalized univalent). Then by part (e), the second coefficient a_2(H_j) satisfies |a_2(H_j)| <= 2. But a_2(H_j) = z_j - c_0. So |z_j - c_0| <= 2. Then |z_1 - z_2| <= |z_1 - c_0| + |c_0 - z_2| <= 4.\n\nThus part (f) is proved.\n\nBut we need to be careful: part (e) says |a_2| <= 2 for any normalized univalent function. So we can apply it to H_j. However, H_j is defined on D and is injective. So yes.\n\nAlternatively, we could apply part (c) directly to h(z) - z_j? But h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . This is of the form required in (c). Then the coefficient c_1 in (c) is c_1 (the same for both j). That doesn't give a relation between z_1 and z_2. So the hint about 1/(h(z) - z_j) is the right approach.\n\nWait, the hint says \"Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).\" That matches our H_j. The second coefficient is the coefficient of z^2? Or coefficient of z^1? Usually \"second coefficient\" might mean the coefficient of z^1 (the linear term) or z^2? In the expansion H_j(z) = z + a_2 z^2 + ..., the second coefficient is a_2. So that's consistent.\n\nThus part (f) is done.\n\nPart (g): Complete the proof of the theorem.\n\nWe need to show that for f injective, f(0)=0, f'(0)=1, we have D_{1/4}(0) subset f(D). The hint: If f avoids w, then 1/f avoids 0 and 1/w.\n\nSuppose there exists w with |w| < 1/4 such that w not in f(D). Consider the function h(z) = 1/f(z). Since f is injective and f(0)=0, f(z) != 0 for z != 0. So h is defined and holomorphic on D \\ {0}. Near 0, f(z) ~ z, so h(z) ~ 1/z. So h has a simple pole at 0. Also h is injective on D \\ {0} (since f is injective and nonzero away from 0). So h satisfies the hypotheses of part (c) and (f). Moreover, h avoids 0 (since f(z) is finite and nonzero for z != 0, so 1/f(z) != 0). And h avoids 1/w (since f avoids w). So h avoids 0 and 1/w. Then by part (f), |0 - 1/w| <= 4, i.e., 1/|w| <= 4, so |w| >= 1/4. Contradiction. Therefore no such w exists, so D_{1/4}(0) subset f(D).\n\nWe also need to show that 1/4 is best possible, i.e., there exists a function for which the image omits a point at distance exactly 1/4 from the origin. The Koebe function f(z) = z/(1-z)^2 is such an example. It omits the value -1/4. Let's verify: f(z) = z/(1-z)^2. For z in D, does it omit -1/4? Solve z/(1-z)^2 = -1/4 => 4z = -(1-z)^2 = -(1 - 2z + z^2) = -1 + 2z - z^2 => z^2 + 2z + 1 = 0 => (z+1)^2 = 0 => z = -1. But z = -1 is on the boundary, not in D. So -1/4 is omitted. And |-1/4| = 1/4. So the radius 1/4 is sharp.\n\nThus the theorem is proved.\n\nNow we need to write a complete solution with full proofs for each part (a)-(g). We should be careful to include all details, justifications, and reasoning.\n\nLet's structure the solution:\n\n- Introduction: Define D, state the problem.\n\n- Part (a): Provide the sequence f_n(z) = z/n. Show f_n(0)=0, holomorphic. Show 1/n not in f_n(D). Compute f_n'(0) = 1/n -> 0. Conclude no uniform r exists.\n\n- Part (b): Provide f_epsilon(z) = epsilon(e^{z/epsilon} - 1). Show f_epsilon(0)=0, f_epsilon'(0)=1. Show f_epsilon(D) omits -epsilon. Conclude no uniform r exists.\n\n- Part (c): State the area theorem. Compute the area of the complement of h(D_rho \\ {0}) using the parametric formula. Derive the inequality sum n|c_n|^2 <= 1.\n\n- Part (d): Construct psi as holomorphic square root of f(z)/z. Define g(z) = z psi(z^2). Show g(0)=0, g'(0)=1, g injective, and g^2(z) = f(z^2).\n\n- Part (e): Use g from (d). Note g is odd, so 1/g has expansion 1/z + c_1 z + ... . Apply (c) to 1/g to get |c_1| <= 1. Relate c_1 to a_2: c_1 = -a_2/2. Thus |a_2| <= 2. Equality case: forces 1/g(z) = 1/z + e^{i theta} z, leading to g(z) = z/(1 + e^{i theta} z^2), and f(z) = z/(1 - e^{i theta} z)^2 (adjusting theta).\n\n- Part (f): For h avoiding z_1, z_2, define H_j(z) = 1/(h(z) - z_j). Show H_j is normalized univalent. Its second coefficient is z_j - c_0. By part (e), |z_j - c_0| <= 2. Then triangle inequality gives |z_1 - z_2| <= 4.\n\n- Part (g): Suppose f avoids w with |w| < 1/4. Then h = 1/f avoids 0 and 1/w. Apply (f) to h: |0 - 1/w| <= 4 => |w| >= 1/4, contradiction. Hence D_{1/4}(0) subset f(D). Show sharpness with Koebe function.\n\nWe need to ensure all steps are rigorous. Let's write out the details.\n\nPart (a) details:\n\nDefine f_n(z) = z/n for n >= 1. Then f_n is holomorphic on D, f_n(0) = 0. The image f_n(D) = {z/n : |z| < 1} = D_{1/n}(0). The point 1/n has modulus 1/n, so it lies on the boundary of f_n(D), not in the open disc. Thus 1/n not in f_n(D). However, 1/n is in D_r(0) for any r > 1/n. So for any candidate r > 0, choose n > 1/r. Then 1/n < r, so 1/n in D_r(0), but 1/n not in f_n(D). Hence D_r(0) not subset of f_n(D). Therefore no such r exists.\n\nCompute f_n'(0) = 1/n. As n -> infinity, f_n'(0) -> 0. This shows that the condition f'(0) = 1 is essential to prevent the derivative from shrinking, which would allow the image to be arbitrarily small near the origin.\n\nPart (b) details:\n\nDefine f_epsilon(z) = epsilon(e^{z/epsilon} - 1) for epsilon > 0. Then f_epsilon(0) = epsilon(1-1) = 0. f_epsilon'(z) = epsilon * (1/epsilon) e^{z/epsilon} = e^{z/epsilon}. So f_epsilon'(0) = 1. The function is entire, hence holomorphic on D. Since e^{z/epsilon} never equals 0, f_epsilon(z) = -epsilon has no solution. Thus -epsilon not in f_epsilon(D). For any r > 0, choose epsilon < r. Then -epsilon is in D_r(0) (since |-epsilon| = epsilon < r), but -epsilon not in f_epsilon(D). Hence no uniform r works.\n\nNote: The hint suggests this function. It's important to verify that f_epsilon is indeed holomorphic and satisfies the conditions.\n\nPart (c) details:\n\nLet h(z) = 1/z + sum_{n=0}^\\infty c_n z^n, analytic and injective for 0 < |z| < 1. For 0 < rho < 1, consider the image of the punctured disc D_rho^* = {z: 0 < |z| < rho}. Since h is injective, the image h(D_rho^*) is a domain. The boundary of this domain includes the image of the circle |z| = rho. Because h has a simple pole at 0, the image of a small circle around 0 is a large curve that encloses the complement. The complement of h(D_rho^*) in C is a compact set K_rho (the bounded component of the complement). The area of K_rho can be computed using the formula for the area enclosed by a parametric curve.\n\nThe curve is gamma_rho(theta) = h(rho e^{i theta}) for theta in [0, 2pi]. Since h is injective, gamma_rho is a simple closed curve. The orientation is clockwise because h(z) ~ 1/z near 0. The area of the interior (which is K_rho) is given by\n\nArea(K_rho) = (1/2) |Im integral_0^{2pi} overline{gamma_rho} gamma_rho' d theta|.\n\nBut we can compute the signed area:\n\nA_signed = (1/2i) integral_0^{2pi} overline{gamma_rho} gamma_rho' d theta.\n\nSince the curve is clockwise, A_signed = -Area(K_rho).\n\nCompute the integral:\n\ngamma_rho(theta) = rho^{-1} e^{-i theta} + sum_{n=0}^\\infty c_n rho^n e^{i n theta}.\ngamma_rho'(theta) = -i rho^{-1} e^{-i theta} + sum_{n=1}^\\infty i n c_n rho^n e^{i n theta}.\n\nThen overline{gamma_rho} gamma_rho' = [rho^{-1} e^{i theta} + sum_{m=0}^\\infty overline{c_m} rho^m e^{-i m theta}] * [-i rho^{-1} e^{-i theta} + sum_{n=1}^\\infty i n c_n rho^n e^{i n theta}].\n\nMultiplying and integrating term by term, only the constant terms survive. The constant term from the product of the first terms is -i rho^{-2}. The constant term from the product of the series terms occurs when n = m, giving i n |c_n|^2 rho^{2n}. There are no cross terms that give constant exponent because the exponents are (n+1) and -(m+1), which are never zero for n>=1, m>=0. Thus\n\nintegral_0^{2pi} overline{gamma_rho} gamma_rho' d theta = 2pi (-i rho^{-2}) + 2pi i sum_{n=1}^\\infty n |c_n|^2 rho^{2n} = 2pi i (sum_{n=1}^\\infty n |c_n|^2 rho^{2n} - rho^{-2}).\n\nTherefore\n\nA_signed = (1/2i) * 2pi i (sum n|c_n|^2 rho^{2n} - rho^{-2}) = pi (sum n|c_n|^2 rho^{2n} - rho^{-2}).\n\nSince the curve is clockwise, Area(K_rho) = -A_signed = pi (rho^{-2} - sum_{n=1}^\\infty n |c_n|^2 rho^{2n}).\n\nSince Area(K_rho) >= 0, we have sum_{n=1}^\\infty n |c_n|^2 rho^{2n} <= rho^{-2} for all rho in (0,1). Letting rho -> 1^- gives sum_{n=1}^\\infty n |c_n|^2 <= 1.\n\nThis completes part (c).\n\nPart (d) details:\n\nGiven f(z) = z + a_2 z^2 + ... injective on D. Since f is injective and f(0)=0, f(z) != 0 for z != 0. Thus f(z)/z != 0 for all z in D. Also f(z)/z is holomorphic on D (removable singularity at 0, with value f'(0)=1). Since D is simply connected and f(z)/z is nowhere zero, there exists a holomorphic function psi on D such that psi(z)^2 = f(z)/z. We choose the branch with psi(0) = 1 (since f(z)/z -> 1 as z->0). Define g(z) = z psi(z^2). Then g(0) = 0. Compute g'(z): g'(z) = psi(z^2) + z * psi'(z^2) * 2z. At z=0, g'(0) = psi(0) = 1. So g'(0)=1.\n\nCheck injectivity: Suppose g(z1) = g(z2). Then z1 psi(z1^2) = z2 psi(z2^2). Squaring both sides: z1^2 psi(z1^2)^2 = z2^2 psi(z2^2)^2. But psi(z^2)^2 = f(z^2)/z^2. So z1^2 * f(z1^2)/z1^2 = z2^2 * f(z2^2)/z2^2, giving f(z1^2) = f(z2^2). Since f is injective, z1^2 = z2^2. Thus z2 = epsilon z1 with epsilon = +/- 1. If epsilon = 1, done. If epsilon = -1, then z2 = -z1. Then g(z2) = g(-z1) = -z1 psi((-z1)^2) = -z1 psi(z1^2) = -g(z1). Since g(z1) = g(z2) = -g(z1), we get 2g(z1) = 0, so g(z1) = 0. But g(z) = 0 implies z psi(z^2) = 0, so z=0 (since psi(z^2) = sqrt{f(z^2)/z^2} != 0 for z != 0). Thus z1 = 0, so z2 = 0. Hence g is injective.\n\nFinally, g^2(z) = z^2 psi(z^2)^2 = z^2 * f(z^2)/z^2 = f(z^2). So g satisfies the hypotheses and g^2(z) = f(z^2).\n\nPart (e) details:\n\nFrom part (d), g is odd: g(-z) = -z psi((-z)^2) = -z psi(z^2) = -g(z). So g(z) = z + b_3 z^3 + b_5 z^5 + ... . The relation f(z^2) = g(z)^2 gives:\n\nf(z^2) = z^2 + a_2 z^4 + a_3 z^6 + ... = (z + b_3 z^3 + ...)^2 = z^2 + 2 b_3 z^4 + ... . Comparing coefficients of z^4: a_2 = 2 b_3. So b_3 = a_2/2.\n\nNow consider h(z) = 1/g(z). Since g is injective and g(0)=0, g(z) != 0 for z != 0. Thus h is holomorphic and injective on D \\ {0}. It has a simple pole at 0: h(z) = 1/z + d_0 + d_1 z + ... . Since g is odd, h is odd: h(-z) = 1/g(-z) = -1/g(z) = -h(z). Thus the Laurent expansion of h has only odd powers: h(z) = 1/z + d_1 z + d_3 z^3 + ... . So d_0 = 0, d_2 = 0, etc.\n\nApply part (c) to h. The coefficients are c_0 = d_0 = 0, c_1 = d_1, c_2 = 0, ... . Then sum_{n=1}^\\infty n |c_n|^2 = |d_1|^2 + 3|d_3|^2 + ... <= 1. In particular, |d_1| <= 1.\n\nNow compute d_1 from g. Since g(z) = z (1 + (a_2/2) z^2 + ... ), we have\n\n1/g(z) = (1/z) * (1 + (a_2/2) z^2 + ... )^{-1} = (1/z) * (1 - (a_2/2) z^2 + ... ) = 1/z - (a_2/2) z + ... .\n\nThus d_1 = -a_2/2. Therefore |a_2/2| <= 1, so |a_2| <= 2.\n\nEquality |a_2| = 2 implies |d_1| = 1. Then the sum in part (c) is >= |d_1|^2 = 1, so equality holds throughout: all other c_n = 0. Thus h(z) = 1/z + d_1 z with |d_1| = 1. Write d_1 = -e^{i theta} (or e^{i theta} depending on sign). Then 1/g(z) = 1/z - e^{i theta} z (absorbing sign into theta). Solving for g: g(z) = z/(1 + e^{i theta} z^2). Then f(z^2) = g(z)^2 = z^2/(1 + e^{i theta} z^2)^2. Replacing z^2 by z, we get f(z) = z/(1 + e^{i theta} z)^2. Letting e^{i phi} = -e^{i theta}, we can write f(z) = z/(1 - e^{i phi} z)^2. Conversely, for any such f, one checks that |a_2| = 2 (since a_2 = 2 e^{i theta} for f(z) = z/(1 - e^{i theta} z)^2). This completes part (e).\n\nPart (f) details:\n\nLet h(z) = 1/z + c_0 + c_1 z + ... be injective on D and avoid z_1 and z_2. For each j = 1,2, define\n\nH_j(z) = 1/(h(z) - z_j).\n\nSince h avoids z_j, the denominator never vanishes. Since h has a simple pole at 0, h(z) - z_j has a simple pole at 0, so H_j has a simple zero at 0. Moreover, H_j is injective: if H_j(z1) = H_j(z2), then h(z1) - z_j = h(z2) - z_j, so h(z1) = h(z2), so z1 = z2 by injectivity of h. Also H_j is holomorphic on D. Compute the expansion:\n\nh(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... .\n\nThus\n\nH_j(z) = 1 / (1/z + (c_0 - z_j) + c_1 z + ... ) = z / (1 + (c_0 - z_j) z + c_1 z^2 + ... ) = z (1 - (c_0 - z_j) z + ... ) = z - (c_0 - z_j) z^2 + ... .\n\nSo H_j(z) = z + a_2^{(j)} z^2 + ... with a_2^{(j)} = -(c_0 - z_j) = z_j - c_0.\n\nThus H_j is a normalized univalent function (injective, H_j(0)=0, H_j'(0)=1). By part (e), |a_2^{(j)}| <= 2. Hence |z_j - c_0| <= 2 for j=1,2. By the triangle inequality,\n\n|z_1 - z_2| <= |z_1 - c_0| + |z_2 - c_0| <= 2 + 2 = 4.\n\nThis completes part (f).\n\nPart (g) details:\n\nLet f be injective on D with f(0)=0, f'(0)=1. Suppose for contradiction that there exists w in C with |w| < 1/4 and w not in f(D). Consider the function\n\nh(z) = 1/f(z), defined for z in D \\ {0}. Since f is injective and f(0)=0, f(z) != 0 for z != 0, so h is holomorphic and injective on D \\ {0}. Near 0, f(z) = z + O(z^2), so h(z) = 1/z + O(1). Thus h has a simple pole at 0 and can be written as h(z) = 1/z + C_0 + C_1 z + ... . Since f avoids w, h avoids 1/w. Also h avoids 0 because f(z) is finite and nonzero for z != 0. Thus h avoids 0 and 1/w.\n\nApply part (f) to h with z_1 = 0 and z_2 = 1/w. Then |0 - 1/w| <= 4, i.e., 1/|w| <= 4, so |w| >= 1/4. This contradicts |w| < 1/4. Therefore no such w exists, and D_{1/4}(0) subset f(D).\n\nTo see that 1/4 is best possible, consider the Koebe function\n\nK(z) = z/(1 - z)^2 = sum_{n=1}^\\infty n z^n.\n\nIt is injective on D, K(0)=0, K'(0)=1. Its image is C \\ (-infty, -1/4]. In particular, it omits the value -1/4, which has modulus 1/4. Thus the radius cannot be increased.\n\nThis completes the proof of the Koebe-Bieberbach theorem.\n\nNow we need to write this in a clear, rigorous manner. We should also ensure that we address the \"compute f_n'(0), and discuss\" part in (a). We have f_n'(0) = 1/n -> 0. The discussion is that without a lower bound on f'(0), the image can be shrunk arbitrarily.\n\nAlso, in part (b), we should compute f_epsilon'(0) = 1, as required.\n\nWe should also ensure that in part (c), we justify the area formula carefully. The area of the complement is nonnegative, leading to the inequality.\n\nIn part (d), we need to verify that g is indeed injective. The argument using squaring is good.\n\nIn part (e), we need to be careful about the equality case. The area theorem equality case: if sum n|c_n|^2 = 1, then the area of the complement is zero. This implies that the image of the circle |z|=rho has area zero in the limit? Actually, the area of the complement is pi(1/rho^2 - sum n|c_n|^2 rho^{2n}). If sum n|c_n|^2 = 1, then the area is pi(1/rho^2 - rho^2). As rho->1, this tends to 0. But for each rho<1, the area is positive unless the sum is exactly 1/rho^2? Wait, the inequality is sum n|c_n|^2 rho^{2n} <= 1/rho^2. If sum n|c_n|^2 = 1, then for rho<1, sum n|c_n|^2 rho^{2n} < sum n|c_n|^2 = 1 <= 1/rho^2? Actually, 1/rho^2 > 1. So the inequality is strict for rho<1. The area is pi(1/rho^2 - sum n|c_n|^2 rho^{2n}) > 0 unless the sum equals 1/rho^2. But sum n|c_n|^2 = 1 does not imply sum n|c_n|^2 rho^{2n} = 1/rho^2. So the area is positive for each rho<1. However, the equality case in the coefficient bound |c_1| <= 1 from sum n|c_n|^2 <= 1 occurs when all other c_n = 0 and |c_1| = 1. Because if any other c_n != 0, then sum n|c_n|^2 > |c_1|^2, so if |c_1|=1, the sum would exceed 1. Thus equality |c_1|=1 forces c_n = 0 for n >= 2. So h(z) = 1/z + c_1 z. This is the equality case.\n\nThus the argument in part (e) is valid: if |a_2| = 2, then |d_1| = 1, so sum n|c_n|^2 >= |d_1|^2 = 1, but sum <= 1, so equality holds, forcing all other coefficients zero.\n\nWe should also verify that the function h(z) = 1/z + c_1 z is indeed injective on the punctured disc. For |c_1|=1, h(z) = (1 + c_1 z^2)/z. If h(z1) = h(z2), then (1 + c_1 z1^2)/z1 = (1 + c_1 z2^2)/z2 => z2 + c_1 z1^2 z2 = z1 + c_1 z1 z2^2 => (z2 - z1) + c_1 z1 z2 (z1 - z2) = 0 => (z2 - z1)(1 - c_1 z1 z2) = 0. So either z1 = z2 or z1 z2 = 1/c_1. Since |z1|<1, |z2|<1, |z1 z2| < 1, but |1/c_1| = 1, so z1 z2 cannot equal 1/c_1. Thus z1 = z2. So it is injective. Good.\n\nNow, for part (f), we need to ensure that H_j is indeed injective and normalized. We argued that H_j(z) = 1/(h(z) - z_j). Since h is injective, H_j is injective. H_j(0) = 0 because h has a pole at 0. H_j'(0) = 1 because near 0, h(z) ~ 1/z, so h(z) - z_j ~ 1/z, so H_j(z) ~ z. More precisely, H_j(z) = z - (c_0 - z_j) z^2 + ... , so H_j'(0) = 1. So H_j is normalized univalent. Then part (e) applies.\n\nAlternatively, we could apply part (c) directly to h(z) - z_j? Let's see: h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + ... . This is of the form required in (c). Then the coefficient c_1 in (c) is c_1 (the same for both j). That doesn't give a relation between z_1 and z_2. So the hint about 1/(h(z) - z_j) is indeed the right way.\n\nWait, the hint says \"Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).\" That matches H_j. The second coefficient is the coefficient of z^2? Or coefficient of z^1? In the expansion H_j(z) = z + (z_j - c_0) z^2 + ... , the second coefficient (coefficient of z^2) is z_j - c_0. So the hint is exactly that.\n\nThus part (f) is solved.\n\nPart (g) is straightforward using (f).\n\nNow, we need to write the final answer. The user wants a complete solution with proofs for each part (a)-(g). We should present it clearly, with sections for each part, and include all reasoning.\n\nWe should also ensure that we use proper mathematical notation and formatting. Since the problem is from a markdown file with solution tags, we can provide a clean solution.\n\nLet's write the solution.\n\nWe'll start with a brief introduction.\n\nThen for each part:\n\n(a) Provide the sequence f_n(z) = z/n. Show properties. Compute derivative. Conclude.\n\n(b) Provide f_epsilon(z) = epsilon(e^{z/epsilon} - 1). Show properties. Conclude.\n\n(c) Derive area formula. Show inequality.\n\n(d) Construct psi and g. Show injectivity.\n\n(e) Use g to bound a_2. Equality case.\n\n(f) Define H_j. Apply (e). Triangle inequality.\n\n(g) Contradiction using (f). Sharpness with Koebe function.\n\nWe should also mention that the Koebe function is f(z) = z/(1-z)^2.\n\nNow, let's write the solution in detail.\n\nPotential pitfalls:\n\n- In part (c), we need to justify that the area of the complement is given by that formula. We can derive it as above.\n\n- In part (d), we need to justify that psi exists. Since D is simply connected and f(z)/z is nowhere zero, a holomorphic square root exists. We can define psi(z) = exp((1/2) log(f(z)/z)) where log is a holomorphic branch of the logarithm. Since f(z)/z is nonzero and D is simply connected, such a branch exists. We choose the branch with psi(0)=1.\n\n- In part (e), we need to be careful about the equality case. The area theorem gives sum n|c_n|^2 <= 1. If |c_1| = 1, then sum_{n=2}^\\infty n|c_n|^2 = 0, so c_n = 0 for n >= 2. Thus h(z) = 1/z + c_1 z. Then we solve for g and f.\n\n- In part (f), we need to ensure that H_j is indeed univalent (injective). Since h is injective, the map w -> 1/w is injective on the range of h - z_j (which avoids 0). So the composition is injective.\n\n- In part (g), we need to ensure that h = 1/f is injective on D \\ {0}. Since f is injective and f(z) != 0 for z != 0, the map w -> 1/w is injective on the range of f (which avoids 0). So h is injective. Also h has a simple pole at 0. So h satisfies the hypotheses of (c) and (f). Actually, for (f), we need h to be of the form 1/z + ... and injective on D \\ {0}. Yes.\n\nThus the solution is complete.\n\nNow, let's write the final answer.",
    "format": "unknown",
    "index": 0
  }
]
```

---

## Raw Response (truncated)

```json
{
  "id": "gen-1789204012-flHRmdh8HBEYlLxFg0uh",
  "object": "chat.completion",
  "created": 1789204012,
  "model": "inclusionai/ling-3.0-flash-sante:free",
  "provider": "Novita",
  "system_fingerprint": null,
  "service_tier": null,
  "choices": [
    {
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop",
      "native_finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "**Solution.**  \nLet \\(\\mathbb D=\\{z\\in\\mathbb C:|z|<1\\}\\).  A holomorphic injection on \\(\\mathbb D\\) is called *univalent*.  \nThe normalisation \\(f(0)=0,\\;f'(0)=1\\) will be assumed whenever it is stated.\n\n---------------------------------------------------------------------\n\n### (a)  No uniform \\(r\\) without extra hypotheses\n\nTake  \n\\[\nf_n(z)=\\frac{z}{n}\\qquad (n=1,2,\\dots ).\n\\]\nEach \\(f_n\\) is holomorphic on \\(\\mathbb D\\) and \\(f_n(0)=0\\).  \nThe image is the open disc of radius \\(1/n\\):\n\\[\nf_n(\\mathbb D)=\\Bigl\\{\\frac{z}{n}:|z|<1\\Bigr\\}=D_{1/n}(0).\n\\]\nHence the point \\(1/n\\) (which lies in \\(D_r(0)\\) for every \\(r>1/n\\)) is **not** in \\(f_n(\\mathbb D)\\).  \nFor any candidate radius \\(r>0\\) choose \\(n>1/r\\); then \\(1/n\\in D_r(0)\\setminus f_n(\\mathbb D)\\), so\n\\(D_r(0)\\not\\subseteq f_n(\\mathbb D)\\).  Thus no single \\(r\\) works for all holomorphic \\(f\\) with \\(f(0)=0\\).\n\nThe derivative at the origin is \\(f_n'(0)=1/n\\to 0\\).  This shows that the condition \\(f'(0)=1\\) is essential: without it the map can shrink the disc arbitrarily near the origin.\n\n---------------------------------------------------------------------\n\n### (b)  The condition \\(f'(0)=1\\) is still not enough\n\nFor \\(\\epsilon>0\\) define  \n\\[\nf_\\epsilon(z)=\\epsilon\\bigl(e^{z/\\epsilon}-1\\bigr).\n\\]\nThen \\(f_\\epsilon(0)=0\\) and \\(f_\\epsilon'(0)=e^0=1\\).  The function is entire, hence holomorphic on \\(\\mathbb D\\).  \nSince \\(e^{z/\\epsilon}\\neq 0\\) for all \\(z\\), we have \\(f_\\epsilon(z)\\neq -\\epsilon\\); thus \\(-\\epsilon\\notin f_\\epsilon(\\mathbb D)\\).\n\nGiven any \\(r>0\\), choose \\(\\epsilon<r\\).  Then \\(-\\epsilon\\in D_r(0)\\) but \\(-\\epsilon\\notin f_\\epsilon(\\mathbb D)\\).  \nHence no uniform \\(r\\) exists even when \\(f'(0)=1\\).\n\n---------------------------------------------------------------------\n\n### (c)  The area theorem\n\nLet  \n\\[\nh(z)=\\frac1z+c_0+c_1z+c_2z^2+\\cdots\n\\]\nbe analytic and injective for \\(0<|z|<1\\).  Fix \\(0<\\rho<1\\) and consider the punctured disc\n\\(D_\\rho^*=\\{z:0<|z|<\\rho\\}\\).  Because \\(h\\) is injective, the image \\(h(D_\\rho^*)\\) is a domain.\nThe boundary of the complement consists of the curve \\(\\gamma_\\rho(\\theta)=h(\\rho e^{i\\theta})\\),\ntraversed clockwise (since \\(h(z)\\sim 1/z\\) near \\(0\\)).  The bounded component of the complement,\ncall it \\(K_\\rho\\), is a compact set whose area we compute.\n\nThe signed area enclosed by a closed curve \\(w(\\theta)\\) is \\(\\frac1{2i}\\int_0^{2\\pi}\\overline{w}\\,w'\\,d\\theta\\).\nFor a clockwise curve this equals \\(-\\operatorname{Area}(K_\\rho)\\).  Using the series,\n\\[\n\\begin{aligned}\n\\gamma_\\rho(\\theta)&=\\rho^{-1}e^{-i\\theta}+\\sum_{n=0}^\\infty c_n\\rho^n e^{in\\theta},\\\\\n\\gamma_\\rho'(\\theta)&=-i\\rho^{-1}e^{-i\\theta}+\\sum_{n=1}^\\infty in c_n\\rho^n e^{in\\theta}.\n\\end{aligned}\n\\]\nMultiplying and integrating, only terms with exponent \\(0\\) survive:\n\\[\n\\int_0^{2\\pi}\\overline{\\gamma_\\rho}\\,\\gamma_\\rho'\\,d\\theta\n=2\\pi i\\Bigl(\\sum_{n=1}^\\infty n|c_n|^2\\rho^{2n}-\\rho^{-2}\\Bigr).\n\\]\nHence\n\\[\n\\operatorname{Area}(K_\\rho)=-\\frac1{2i}\\int_0^{2\\pi}\\overline{\\gamma_\\rho}\\,\\gamma_\\rho'\\,d\\theta\n=\\pi\\Bigl(\\rho^{-2}-\\sum_{n=1}^\\infty n|c_n|^2\\rho^{2n}\\Bigr).\n\\]\nSince area is non\u2011negative,\n\\[\n\\sum_{n=1}^\\infty n|c_n|^2\\rho^{2n}\\le \\rho^{-2}\\qquad(0<\\rho<1).\n\\]\nLetting \\(\\rho\\to1^-\\) (monotone convergence) yields\n\\[\n\\boxed{\\sum_{n=1}^\\infty n|c_n|^2\\le 1}.\n\\]\n\n---------------------------------------------------------------------\n\n### (d)  Constructing an odd square root\n\nLet \\(f(z)=z+a_2z^2+\\cdots\\) be univalent on \\(\\mathbb D\\).  \nBecause \\(f\\) is injective and \\(f(0)=0\\), we have \\(f(z)\\neq0\\) for \\(z\\neq0\\); thus\n\\(f(z)/z\\neq0\\) on \\(\\mathbb D\\).  The function \\(f(z)/z\\) is holomorphic on the simply connected\ndomain \\(\\mathbb D\\) and nowhere zero, so it possesses a holomorphic square root \\(\\psi\\) with\n\\(\\psi(0)=1\\):\n\\[\n\\psi(z)^2=\\frac{f(z)}{z}.\n\\]\nDefine\n\\[\ng(z)=z\\,\\psi(z^2).\n\\]\nThen \\(g(0)=0\\) and\n\\[\ng'(0)=\\psi(0)=1.\n\\]\nInjectivity of \\(g\\): if \\(g(z_1)=g(z_2)\\), squaring gives\n\\(z_1^2\\psi(z_1^2)^2=z_2^2\\psi(z_2^2)^2\\), i.e. \\(f(z_1^2)=f(z_2^2)\\).\nBy injectivity of \\(f\\), \\(z_1^2=z_2^2\\), so \\(z_2=\\pm z_1\\).  If \\(z_2=-z_1\\) then\n\\(g(z_2)=g(-z_1)=-g(z_1)\\), forcing \\(g(z_1)=0\\) and hence \\(z_1=0\\).  Thus \\(z_1=z_2\\).\nFinally,\n\\[\ng(z)^2=z^2\\psi(z^2)^2=z^2\\frac{f(z^2)}{z^2}=f(z^2).\n\\]\nSo \\(g\\) satisfies the same normalisation and is univalent, and \\(g^2(z)=f(z^2)\\).\n\n---------------------------------------------------------------------\n\n### (e)  The second coefficient satisfies \\(|a_2|\\le 2\\)\n\nFrom part (d), \\(g\\) is odd: \\(g(-z)=-g(z)\\).  Hence its expansion contains only odd powers:\n\\[\ng(z)=z+b_3z^3+b_5z^5+\\cdots.\n\\]\nComparing \\(f(z^2)=g(z)^2\\) gives \\(a_2=2b_3\\).\n\nNow consider \\(h(z)=1/g(z)\\).  Since \\(g\\) is univalent and \\(g(0)=0\\), \\(h\\) is analytic and\ninjective on \\(0<|z|<1\\) with a simple pole at \\(0\\):\n\\[\nh(z)=\\frac1z+d_0+d_1z+d_2z^2+\\cdots.\n\\]\nBecause \\(g\\) is odd, \\(h\\) is odd, so \\(d_0=d_2=\\cdots=0\\):\n\\[\nh(z)=\\frac1z+d_1z+\\cdots.\n\\]\nApplying part (c) to \\(h\\) gives \\(|d_1|\\le 1\\).\n\nTo relate \\(d_1\\) to \\(a_2\\), expand \\(1/g\\):\n\\[\ng(z)=z\\Bigl(1+\\frac{a_2}{2}z^2+\\cdots\\Bigr)\\quad\\Longrightarrow\\quad\n\\frac1{g(z)}=\\frac1z\\Bigl(1-\\frac{a_2}{2}z^2+\\cdots\\Bigr)=\\frac1z-\\frac{a_2}{2}z+\\cdots.\n\\]\nThus \\(d_1=-a_2/2\\), and \\(|a_2|=2|d_1|\\le 2\\).\n\n**Equality case.**  If \\(|a_2|=2\\) then \\(|d_1|=1\\).  In the inequality of part (c),\n\\(\\sum n|c_n|^2\\ge |d_1|^2=1\\); together with \\(\\sum n|c_n|^2\\le1\\) this forces\n\\(c_n=0\\) for all \\(n\\ge2\\) and \\(|c_1|=1\\).  Hence \\(h(z)=1/z+d_1z\\) with \\(|d_1|=1\\).\nWriting \\(d_1=-e^{i\\theta}\\) and solving for \\(g\\):\n\\[\n\\frac1{g(z)}=\\frac1z-e^{i\\theta}z\\;\\Longrightarrow\\;\ng(z)=\\frac{z}{1+e^{i\\theta}z^2}.\n\\]\nThen\n\\[\nf(z^2)=g(z)^2=\\frac{z^2}{(1+e^{i\\theta}z^2)^2}\n\\;\\Longrightarrow\\;\nf(z)=\\frac{z}{(1+e^{i\\theta}z)^2}.\n\\]\nReplacing \\(e^{i\\theta}\\) by \\(e^{-i\\theta}\\) gives the stated form\n\\(f(z)=z/(1-e^{i\\theta}z)^2\\).  Conversely, for such \\(f\\) one computes \\(a_2=2e^{i\\theta}\\),\nso \\(|a_2|=2\\).\n\n---------------------------------------------------------------------\n\n### (f)  Two omitted values are at distance at most \\(4\\)\n\nLet \\(h(z)=1/z+c_0+c_1z+\\cdots\\) be injective on \\(\\mathbb D\\) and suppose \\(h\\) avoids\n\\(z_1\\) and \\(z_2\\).  For \\(j=1,2\\) define\n\\[\nH_j(z)=\\frac1{h(z)-z_j}.\n\\]\nBecause \\(h\\) avoids \\(z_j\\), the denominator never vanishes; because \\(h\\) has a simple pole\nat \\(0\\), \\(H_j\\) has a simple zero at \\(0\\).  Injectivity of \\(h\\) implies injectivity of\n\\(H_j\\).  Expanding near \\(0\\):\n\\[\nh(z)-z_j=\\frac1z+(c_0-z_j)+c_1z+\\cdots\n\\;\\Longrightarrow\\;\nH_j(z)=\\frac{z}{1+(c_0-z_j)z+\\cdots}=z+(z_j-c_0)z^2+\\cdots.\n\\]\nThus \\(H_j\\) is normalised univalent: \\(H_j(0)=0,\\;H_j'(0)=1\\).  By part (e), the second\ncoefficient satisfies \\(|z_j-c_0|\\le 2\\) for each \\(j\\).  Therefore\n\\[\n|z_1-z_2|\\le|z_1-c_0|+|z_2-c_0|\\le 2+2=4.\n\\]\n\n---------------------------------------------------------------------\n\n### (g)  Proof of the
```
