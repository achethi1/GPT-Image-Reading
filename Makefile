TARGET = Honors_Contract

$(TARGET): $(TARGET).py
	cp ./$(TARGET).py info
	chmod +x info