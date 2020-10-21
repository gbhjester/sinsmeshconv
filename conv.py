import sys

numMaterials = 0
mats = []
numVerts = 0
verts = []
numTris = 0
tris = []

if len(sys.argv) != 3:
    print("Usage : python conv.py path/to/inmesh.mesh outpath")
    exit()

print(sys.argv[1].rsplit(".", 1)[0])

infn = sys.argv[1].rsplit(".")[0]

inf = open(infn + ".mesh")

# Read text .mesh
for line in inf:
	line = line.lstrip().lower()
	if line.startswith("nummaterials"):
		numMaterials = line.split("\040")[1]
	if line.startswith("material"):
		line = inf.readline().lstrip()
		mat = line.split("\"")[1].split("\"")[0].rsplit(".", 1)[0]
		mats.append(mat)
	elif line.startswith("numvertices"):
		numVerts = line.split("\040")[1]
	elif line.startswith("vertex"):
		line = inf.readline().lstrip().lower()
		pos = line.split("[")[1].split("]")[0].strip()
		line = inf.readline().lstrip().lower()
		nrm = line.split("[")[1].split("]")[0].strip()
		inf.readline()
		inf.readline()
		line = inf.readline().strip().lower()
		u0 = line.split("\040")[1]
		line = inf.readline().strip().lower()
		v0 = line.split("\040")[1]
		verts.append((pos, nrm, u0, v0))
	elif line.startswith("numtriangles"):
		numTris = line.split("\040")[1]
	elif line.startswith("triangle"):
		line = inf.readline().strip().lower()
		v0 = line.split("\040")[1]
		line = inf.readline().strip().lower()
		v1 = line.split("\040")[1]
		line = inf.readline().strip().lower()
		v2 = line.split("\040")[1]
		line = inf.readline().strip().lower()
		m = line.split("\040")[1]
		tris.append((v0, v1, v2, m))

#print(numMaterials)
#print(numVerts)
#print(verts)
#print(numTris)
#print(tris)

# Write text .smd
outf = open(infn + ".smd", "w")
outf.write("version 1\n")
outf.write("nodes\n")
outf.write("end\n")
outf.write("time\n")
outf.write("end\n")
outf.write("triangles\n")
for tri in tris:
	v0 = verts[int(tri[0])]
	v1 = verts[int(tri[1])]
	v2 = verts[int(tri[2])]
	outf.write(mats[int(tri[3])] + "\n")
	outf.write(tri[3] + "  " + v0[0] + " " + v0[1] + " " + v0[2] + " " + v0[3] + "\n")
	outf.write(tri[3] + "  " + v1[0] + " " + v1[1] + " " + v1[2] + " " + v1[3] + "\n")
	outf.write(tri[3] + "  " + v2[0] + " " + v2[1] + " " + v2[2] + " " + v2[3] + "\n")
outf.write("end\n")