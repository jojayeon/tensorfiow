import tensorflow as tf
import numpy as np

# 1. 데이터 형태 정의
image_shape = (224, 224, 3)  # 전신 사진의 크기 (224x224, RGB 이미지)
numeric_shape = (3,)         # 체력, 공격력, 방어력 (수치 3개)

# 2. 이미지 입력 정의
image_input = tf.keras.layers.Input(shape=image_shape)

# 3. CNN(합성곱 신경망)으로 이미지 처리
x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(image_input)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)
x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)
x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)
x = tf.keras.layers.Flatten()(x)

# 4. 수치형 데이터 입력 (체력, 공격력, 방어력)
numeric_input = tf.keras.layers.Input(shape=numeric_shape)
y = tf.keras.layers.Dense(64, activation='relu')(numeric_input)

# 5. 이미지 처리 결과와 수치형 데이터 결합
combined = tf.keras.layers.concatenate([x, y])

# 6. 결합된 데이터를 Dense 레이어로 처리
z = tf.keras.layers.Dense(128, activation='relu')(combined)
z = tf.keras.layers.Dense(64, activation='relu')(z)

# 7. 최종 출력층 (이진 분류를 위한 sigmoid 함수 사용)
output = tf.keras.layers.Dense(1, activation='sigmoid')(z)

# 8. 모델 생성
model = tf.keras.models.Model(inputs=[image_input, numeric_input], outputs=output)

# 9. 모델 컴파일 (이진 분류를 위한 손실 함수와 옵티마이저 설정)
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 10. 가짜 데이터 생성
X_images = np.random.random((10, 224, 224, 3))  # 10개의 가짜 이미지 데이터 (224x224 크기)
X_numerics = np.random.random((10, 3))          # 10개의 가짜 수치형 데이터 (체력, 공격력, 방어력)
y_labels = np.random.randint(2, size=(10, 1))   # 10개의 가짜 레이블 (0 또는 1)

# 11. 모델 학습
model.fit([X_images, X_numerics], y_labels, epochs=5)

# 12. 모델 요약 출력
model.summary()
