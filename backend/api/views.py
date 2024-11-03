from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def calculate(request):
    try:
        num1 = float(request.data.get('num1'))
        num2 = float(request.data.get('num2'))
        operation = request.data.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return Response({'error': 'Division by zero'}, status=status.HTTP_400_BAD_REQUEST)
            result = num1 / num2
        else:
            return Response({'error': 'Invalid operation'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': result})

    except (ValueError, TypeError):
        return Response({'error': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)
