from django.test import TestCase
from django.utils import timezone
from .models import Job, JobCategory
from companies.models import Company

class JobCategoryTestCase(TestCase):
	"""
	Test job category

	"""

	def setUp(self):
		return JobCategory.objects.create(cat_name = "Information Technology",description = "Information technolgoy")

	def test_job_category(self):
		"""test job category 
		"""
		job = self.setUp()
		self.assertTrue(isinstance(job, JobCategory))
		self.assertEqual(job.__str__(), job.cat_name)


# class JobTestCase(TestCase):

# 	def setUp(self):
# 		Job.objects.create(title="Sr. System Admin", summary = "handle Unix based system configuration",
# 		description = "update and upgrade unix based server",
# 		requirements = 'red hat certified',
# 		category = Category.objects.all()[0],
# 		job_level = "entry",
# 		location = "Kathmandu",
# 		salary = "10000",
# 		expire_at = timezone.now() + timedelta(days=30),
# 		other_info = "should be passionate programmer",
# 		company = Company.objects.all()[0]
# 		)

# 		def test_job_creation(self):
#     		job = self.setUp()
#     		self.assertTrue(isinstance(job, Job))
#     		self.assertEqual(w.__str__(), job.title)

