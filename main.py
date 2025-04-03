def sort(width, height, length, mass):
  volume = width * height * length

  is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
  is_heavy = mass >= 20

  return "REJECTED" if is_bulky and is_heavy else "SPECIAL" if is_bulky or is_heavy else "STANDARD"


# === STANDARD TEST CASE ===
assert sort(10, 10, 10, 5) == "STANDARD"
assert sort(99, 99, 99, 10) == "STANDARD"
assert sort(120, 80, 90, 19.9) == "STANDARD"

# === SPECIAL TEST CASE ( bulky or heavy, but not both) ===
assert sort(150, 50, 50, 10) == "SPECIAL"         # Bulky - dimension
assert sort(50, 50, 50, 25) == "SPECIAL"          # Heavy
assert sort(140, 140, 140, 10) == "SPECIAL"       # Bulky - volume (140³ = 2,744,000)

# === REJECTED TEST CASE (bulky and heavy) ===
assert sort(150, 150, 150, 25) == "REJECTED"      # Overpass all tresholds
assert sort(200, 50, 50, 30) == "REJECTED"        # Bulky - dimension + heavy
assert sort(145, 145, 145, 21) == "REJECTED"      # Bulky - volume + heavy