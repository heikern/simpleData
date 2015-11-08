from App import dataApp
import unittest


class FlaskTestCase(unittest.TestCase):
	def test_index(self):
		tester = dataApp.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code,200)

	# test if a word is included in the response
	def test_index_with_response(self):
		tester = dataApp.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue('Welcome' in response.data)

	# test login with correct credentials
	def test_login_right(self):
		tester = dataApp.test_client(self)
		response = tester.post(
			'/login',
			data = dict(userName='james',password='admin'),
			follow_redirects=True)
		self.assertIn('12', response.data)

	# test login with incorrect credentials
	def test_login_wrong(self):
		tester = dataApp.test_client(self)
		response = tester.post(
			'/login',
			data = dict(userName='heikern',password='admin'),
			follow_redirects=True)
		self.assertIn('please', response.data)

	# test data appears once user logs in
	def test_data_appear_on_login(self):
		tester = dataApp.test_client(self)
		response = tester.post(
			'/login',
			data = dict(userName='james',password='admin'),
			follow_redirects=True)
		self.assertIn('42', response.data)

	# test logout
	def test_logout(self):
		tester = dataApp.test_client(self)
		tester.post(
			'/login',
			data = dict(userName='james',password='admin'),
			follow_redirects=True)
		response = tester.get('/logout', content_type='html/text')
		self.assertIn('Thank you for visiting Simple Data', response.data)

	# test that data is protected
	def test_data_requires_login(self):
		tester = dataApp.test_client(self)
		response = tester.get('/data', follow_redirects=True)
		self.assertIn('please login to view', response.data)


if __name__ == '__main__':
	unittest.main()