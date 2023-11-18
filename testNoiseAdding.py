noise = [2, 5, 3, 10]

client_num = 10        # 2

if len(noise) >= client_num:
    noise = noise[:client_num]
else:
    for i in range(client_num-len(noise)):
        noise.append(0)

print(noise)


def noiseList(noise, client_num=10):
    if len(noise) >= client_num:
        noise = noise[:client_num]
    else:
        for i in range(client_num - len(noise)):
            noise.append(0)

    return noise

noise_levels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
noise = noiseList(noise_levels, 8)
noise_2 = noiseList(noise_levels, 12)
noise_3 = noiseList(noise_levels)
print(noise, noise_2, noise_3)