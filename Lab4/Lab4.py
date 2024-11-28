import torch
import torchvision
from tqdm import tqdm
import matplotlib.pyplot as plt
device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor(),
	torchvision.transforms.Normalize(mean=[0.5], std=[0.5])])
path = './data'

# 下载数据集
train_data = torchvision.datasets.MNIST(path, train=True,  transform=transform, download=True)
test_data  = torchvision.datasets.MNIST(path, train=False, transform=transform, download=True)

from torch.utils.data import DataLoader
batch_size = 256
train_dataloader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
test_dataloader  = DataLoader(dataset=test_data,  batch_size=batch_size, shuffle=False)

class number_recognize(torch.nn.Module):
	def __init__(self):
		super().__init__()
		# Modules will be added to it in the order they are passed in the constructor.
		self.model = torch.nn.Sequential(
			# Input Size = 28x28
			torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1),
			torch.nn.ReLU(),
			torch.nn.MaxPool2d(kernel_size=2, stride=2),
			
			# Size = 14x14
			torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
			torch.nn.ReLU(),
			torch.nn.MaxPool2d(kernel_size=2, stride=2),
			
			# Size = 7x7
			torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
			torch.nn.ReLU(),

			torch.nn.Flatten(),
			torch.nn.Linear(in_features=64*7*7, out_features=128),
			torch.nn.ReLU(),
			torch.nn.Linear(in_features=128, out_features=10),
			torch.nn.Softmax(dim = 1) # 归一化输出概率
		)

	def forward(self, x):
		return self.model(x)
		
model = number_recognize().to(device)
print(model)
loss_f = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(params=model.parameters())

epochs = 10
log_loss = []
log_acc  = []

for epoch in range(1, epochs+1):
	model.train()
	for img,labels in tqdm(train_dataloader):
		img 	= img.to(device)
		labels	= labels.to(device)
		model.zero_grad()
		outputs = model(img)
		loss = loss_f(outputs, labels)
		loss.backward()
		optimizer.step()

	correct_number = 0
	total_loss = 0
	model.eval()
	for (img,labels) in test_dataloader:
		img 	= img.to(device)
		labels	= labels.to(device)
		outputs = model(img)
		loss = loss_f(outputs, labels)
		predictions = torch.argmax(outputs, dim=1)
		
		total_loss += loss
		correct_number += torch.sum(predictions == labels)
	test_accuracy = correct_number / (batch_size * len(test_dataloader))
	test_loss = total_loss/len(test_dataloader)
	
	print(f'[{epoch}/{epochs}] Loss: {test_loss:.4f}, Acc: {test_accuracy:.4f}')
	log_acc .append(test_accuracy)
	log_loss.append(test_loss)
	
torch.save(model, './number_recognize.pth')
import matplotlib.pyplot as plt
model.eval()
examples = enumerate(test_dataloader)
index, (img, labels) = next(examples)
img 	= img.to(device)
labels 	= labels.to(device)
outputs = model(img)
predict = torch.argmax(outputs, dim=1)

fig = plt.figure()
for i in range(6):
	plt.subplot(2, 3, i+1)
	plt.tight_layout()
	plt.imshow(img[i][0].cpu().clone().numpy(), cmap='gray', interpolation='none')
	plt.title(f'Prediction: {predict[i]}')
	plt.xticks([])
	plt.yticks([])
plt.show()