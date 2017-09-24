def replace(in_path, out_path, pattern, subst):
    f_in = open(in_path,'r')
    f_out = open(out_path,'w')

    text = f_in.readlines()
    for line in text:
        f_out.write(line.replace(pattern,subst))

    f_in.close()
    f_out.close()

replace("D:\Dropbox\Bioinfo\Programmation\Exercices\Zola.txt","D:\Dropbox\Bioinfo\Programmation\Exercices\out.txt", 'et', 'ET')